<template>
	<AppLoading v-if="loading" />

	<AppError v-else-if="error" :message="error.message" />

	<div v-else>
		<h2>{{ post.title }}</h2>
		<p>id: {{ props.id }}, isOdd: {{ isOdd }}</p>
		<p>{{ post.content }}</p>
		<p class="text-muted">
			{{ $dayjs(post.createdAt).format('YYYY. MM. DD MM:mm:ss') }}
		</p>
		<hr class="my-4" />
		<AppError v-if="removeError" :message="removeError.message" />
		<div class="row g-2">
			<div class="col-auto">
				<button class="btn btn-outline-dark" @click="$router.push('/posts/10')">
					이전글
				</button>
			</div>
			<div class="col-auto">
				<button class="btn btn-outline-dark" @click="$router.push('/posts/11')">
					다음글
				</button>
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
				<button
					class="btn btn-outline-danger"
					@click="remove"
					:disabled="removeLoading"
				>
					<template v-if="removeLoading">
						<span
							class="spinner-grow spinner-grow-sm"
							aria-hidden="true"
						></span>
						<span class="visually-hidden" role="status">Loading...</span>
					</template>
					<template v-else> 삭제 </template>
				</button>
			</div>
		</div>
	</div>
</template>

<script setup>
import { onBeforeRouteLeave, onBeforeRouteUpdate, useRouter } from 'vue-router';
import { useAxios } from '@/hooks/useAxios';
import { useAlert } from '@/composables/alert';
import { computed } from 'vue';
import { useNumber } from '@/composables/number';
import { toRefs } from 'vue';
const props = defineProps({
	id: [String, Number],
});

const router = useRouter();
const { vAlert, vSuccess } = useAlert();

// 이렇게 반응형 객체를 그대로 가져가게 되면 다른 곳에서 unref를 해줘야 함(number.js 참고)

// const idRef = toRef(props, 'id');
const { id: idRef } = toRefs(props);
const { isOdd } = useNumber(idRef);

// 아래와 같이 하면 반응형을 잃음...
// const { isOdd } = useNumber(props.id);

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

// url을 반응형으로 만들어서 watchEffect에 감지 되도록 만듬.
const url = computed(() => `/posts/${props.id}`);
const { error, loading, data: post } = useAxios(url);

const {
	error: removeError,
	loading: removeLoading,
	execute,
} = useAxios(
	`/posts/${props.id}`,
	{ method: 'delete' },
	{
		immediate: false,
		onSuccess: () => {
			vSuccess('삭제가 완료되었습니다.');
			router.push({ name: 'PostList' });
		},
		onError: err => {
			vAlert(err.message);
		},
	},
);

// const fetchPost = async () => {
// 	try {
// 		loading.value = true;
// 		const { data } = await getPostById(props.id);
// 		setPost(data);
// 	} catch (err) {
// 		error.value = err;
// 	} finally {
// 		loading.value = false;
// 	}

//전개구문을 통한 객체 복사
// 객체 복사를 안하게 되면, 데이터가 바뀌었을 때 참조하고 있어서 함께 변경되는 문제 발생
// };

// const setPost = ({ title, content, createdAt }) => {
// 	post.value.title = title;
// 	post.value.content = content;
// 	post.value.createdAt = createdAt;
// };

// fetchPost();

const remove = async () => {
	if (confirm('삭제하시겠습니까?') === false) {
		return; // if문이 많아질 때 깊어지는 것을 방지하기위해서,,,
	}
	execute();
};

// console.log('post:', getPostById(id));
const goListPage = () => router.push({ name: 'PostList' });
const goEditPage = () =>
	router.push({ name: 'PostEdit', params: { id: props.id } });

onBeforeRouteUpdate(() => {
	console.log('onBeforeRouteUpdate');
});
onBeforeRouteLeave(() => {
	console.log('onBeforeRouteLeave');
});
</script>
<!-- 참고로 Composition Api는 <script setup></script> 에서 -->
<!-- options API는 <script></script>에서 사용가능 -->
<!-- <script></script>는 setup 함수보다 먼저 실행됨 -->
<script>
export default {
	beforeRouteEnter() {
		console.log('beforeRouteEnter');
	},
};
</script>

<style lang="scss" scoped></style>
