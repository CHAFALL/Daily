<template>
	<div>
		<h2>{{ post.title }}</h2>
		<p>{{ post.content }}</p>
		<p class="text-muted">{{ post.createdAt }}</p>
		<hr class="my-4" />
		<div class="row g-2">
			<div class="col-auto">
				<button class="btn btn-outline-dark">이전글</button>
			</div>
			<div class="col-auto">
				<button class="btn btn-outline-dark">다음글</button>
			</div>
			<div class="col-auto me-auto"></div>
			<div class="col-auto">
				<button class="btn btn-outline-dark" @click="goListPage">목록</button>
			</div>
			<div class="col-auto">
				<button class="btn btn-outline-primary" @click="goEditPage">
					수정
				</button>
			</div>
			<div class="col-auto">
				<button class="btn btn-outline-danger" @click="remove">삭제</button>
			</div>
		</div>
	</div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { getPostById, deletePost } from '@/api/posts';
import { ref } from 'vue';

const props = defineProps({
	id: [String, Number],
});

// const route = useRoute();
const router = useRouter();
// const id = route.params.id;

/**
 * ref
 * 장) 객체 할당 가능
 * 장) 일관성 유지 가능
 * 단) 뒤에 value를 붙여줘야함, ex. form.value.title
 *
 * reactive
 * 단) 객체 할당 불가능
 * 장) 뒤에 value를 안 붙여줘도 됨
 *
 * 결론) 왠만하면 ref를 권장.
 */

const post = ref({
	title: null,
	content: null,
	createdAt: null,
});

const fetchPost = async () => {
	try {
		const { data } = await getPostById(props.id);
		setPost(data);
	} catch (error) {
		console.error(error);
	}

	//전개구문을 통한 객체 복사
	// 객체 복사를 안하게 되면, 데이터가 바뀌었을 때 참조하고 있어서 함께 변경되는 문제 발생
};
const setPost = ({ title, content, createdAt }) => {
	post.value.title = title;
	post.value.content = content;
	post.value.createdAt = createdAt;
};

fetchPost();

const remove = async () => {
	try {
		if (confirm('삭제하시겠습니까?') === false) {
			return; // if문이 많아질 때 깊어지는 것을 방지하기위해서,,,
		}
		await deletePost(props.id);
		router.push({ name: 'PostList' });
	} catch (error) {
		console.error(error);
	}
};

// console.log('post:', getPostById(id));
const goListPage = () => router.push({ name: 'PostList' });
const goEditPage = () =>
	router.push({ name: 'PostEdit', params: { id: props.id } });
</script>

<style lang="scss" scoped></style>
