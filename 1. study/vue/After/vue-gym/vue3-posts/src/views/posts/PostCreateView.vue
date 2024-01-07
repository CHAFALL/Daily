<template>
	<div>
		<h2 @click="visibleForm = !visibleForm">게시글 등록</h2>
		<hr class="my-4" />
		<AppError v-if="error" :message="error.message" />
		<PostForm
			v-if="visibleForm"
			v-model:title="form.title"
			v-model:content="form.content"
			@submit.prevent="save"
		>
			<template #actions>
				<button type="button" class="btn btn-outline-dark" @click="goListPage">
					목록
				</button>

				<!-- 버튼에 type="button"이 있으면 안된다. (submit 이벤트가 발생해야 하므로 default인 submit으로 동작하도록 지워줌) -->
				<button class="btn btn-primary" :disabled="loading">
					<template v-if="loading">
						<span
							class="spinner-grow spinner-grow-sm"
							aria-hidden="true"
						></span>
						<span class="visually-hidden" role="status">Loading...</span>
					</template>
					<template v-else> 저장 </template>
				</button>
			</template>
		</PostForm>
	</div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import PostForm from '@/components/posts/PostForm.vue';
import { useAlert } from '@/composables/alert';
import { useAxios } from '@/hooks/useAxios';

const { vAlert, vSuccess } = useAlert();

const router = useRouter();
const form = ref({
	title: null,
	content: null,
});

// 참고: 객체의 값을 바로 할당하면 반응형을 잃음

// 이렇게 하면 세이브 함수를 눌렀을 때 데이터가 들어가야 하는데 세이브 함수를 누르기도 전에 이 엑시오스 함수가 호출이 됨.. -> 이를 막기위해 immediate 이용
const { error, loading, execute } = useAxios(
	`/posts`,
	{
		method: 'post',
	},
	{
		immediate: false,
		onSuccess: () => {
			router.push({ name: 'PostList' });
			vSuccess('등록이 완료되었습니다.');
		},
		onError: err => {
			vAlert(err.message);
		},
	},
);
const save = async () => {
	execute({
		...form.value,
		createdAt: Date.now(),
	});
};

// const save = async () => {
// 	try {
// 		loading.value = true;
// 		await createPost({
// 			...form.value,
// 			createdAt: Date.now(),
// 		});
// 		router.push({ name: 'PostList' });
// 		vSuccess('등록이 완료되었습니다.');
// 	} catch (err) {
// 		vAlert(err.message);
// 		error.value = err;
// 	} finally {
// 		loading.value = false;
// 	}
// };
const goListPage = () => router.push({ name: 'PostList' });
const visibleForm = ref(true);
</script>

<style lang="scss" scoped></style>
