<template>
	<div>
		<h2>게시글 목록</h2>
		<hr class="my-4" />
		<PostFilter
			v-model:title="params.title_like"
			v-model:limit="params._limit"
		></PostFilter>
		<hr class="my-4" />
		<AppGrid :items="posts">
			<template v-slot="{ item }">
				<PostItem
					:title="item.title"
					:content="item.content"
					:created-at="item.createdAt"
					@click="goPage(item.id)"
					@modal="openModal(item)"
				></PostItem>
			</template>
		</AppGrid>

		<!-- 우리가 페이지네이션을 구현하기 위해서는 total 데이터가 몇개인지를 알아야 한다. -->
		<AppPagination
			:current-page="params._page"
			:page-count="pageCount"
			@page="page => (params._page = page)"
		/>

		<!-- css 충돌 발생해서 해당 모델을 밖으로 빼고픔 -->
		<!-- 이렇 때 쓰는 것이 Teleport이다 -->
		<Teleport to="#modal">
			<PostModal
				v-model="show"
				:title="modalTitle"
				:content="modalContent"
				:created-at="modalCreatedAt"
			/>
		</Teleport>

		<template v-if="posts && posts.length > 0">
			<hr class="my-5" />
			<AppCard>
				<!-- 숫자값을 넘길려면 id앞에 :를 해줘야 하는구나 -->
				<PostDetailView :id="posts[0].id"></PostDetailView>
			</AppCard>
		</template>

		<!-- Teleport는 여러군데 지정가능(참고) -->
		<!-- <Teleport to="#modal">
			<div>Hello World!</div>
		</Teleport> -->
	</div>
</template>

<script setup>
import PostItem from '@/components/posts/PostItem.vue';
import PostDetailView from '@/views/posts/PostDetailView.vue';
import AppCard from '@/components/AppCard.vue';
import { getPosts } from '@/api/posts';
import { computed, ref, watchEffect } from 'vue';
import { useRouter } from 'vue-router';
import AppPagination from '@/components/AppPagination.vue';
import AppGrid from '@/components/AppGrid.vue';
import PostFilter from '@/components/posts/PostFilter.vue';
import PostModal from '@/components/posts/PostModal.vue';

const router = useRouter();
const posts = ref([]);
// pagination
const params = ref({
	_sort: 'createdAt', // 무엇을
	_order: 'desc', // 내림차순
	_limit: 3, // 몇개씩 조회
	_page: 1, // 현재 페이지를 조회
	title_like: '', // 해당 요소 검색 기능
});

// pagination
const totalCount = ref(0);
const pageCount = computed(() =>
	Math.ceil(totalCount.value / params.value._limit),
);

/**
 * promise: 자바스크립트에서 비동기를 처리할 때 사용하는 객체
 * 값을 받을때는 .then()을 뒤에 붙여서 받을 수 있음
 * promose 객체 대신에 사용할 수 있는 것이 async await이 있다.
 * async await: 기능은 동일한데 문법적으로 읽기 쉽도록 처리 가능
 */

const fetchPosts = async () => {
	try {
		const { data, headers } = await getPosts(params.value);
		posts.value = data;
		// 기억나지? -같은거 있으면 구분 안되어서 []로 가져와야 하는 것
		totalCount.value = headers['x-total-count'];
	} catch (error) {
		console.error(error);
	}
	// console.dir(response); // 객체를 로그로 출력할 때는 console.dir를 사용하면 편하단다...

	// getPosts()
	// 	.then(response => {
	// 		console.log('response: ', response);
	// 	})
	// 	.catch(error => {
	// 		console.log('error: ', error);
	// 	});
};
watchEffect(fetchPosts);
// fetchPosts();

const goPage = id => {
	//방법1
	// router.push(`/posts/${id}`);
	//방법2
	router.push({
		name: 'PostDetail',
		params: {
			id,
		},
		// 쿼리랑 해쉬도 가능
	});
};

// modal
const show = ref(false);
const modalTitle = ref('');
const modalContent = ref('');
const modalCreatedAt = ref('');

// item을 구조분해할당으로 받은 것임
const openModal = ({ title, content, createdAt }) => {
	show.value = true;
	modalTitle.value = title;
	modalContent.value = content;
	modalCreatedAt.value = createdAt;
};
</script>

<style lang="scss" scoped></style>
