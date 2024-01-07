<template>
	<!-- 이 show는 외부에서 props로 받을 수 없다. (왜냐하면 props는 내부에서 변경을 하면 안되므로) -->
	<AppModal v-model="show" title="게시글">
		<template #default>
			<div class="row g-3">
				<div class="col-3 text-muted">제목</div>
				<div class="col-9">{{ title }}</div>
				<div class="col-3 text-muted">내용</div>
				<div class="col-9">{{ content }}</div>
				<div class="col-3 text-muted">등록일</div>
				<div class="col-9">
					{{ $dayjs(createdAt).format('YYYY. MM. DD MM:mm:ss') }}
				</div>
			</div>
		</template>
		<template #actions>
			<button type="button" class="btn btn-secondary" @click="closeModal">
				닫기
			</button>
		</template>
	</AppModal>
</template>

<script setup>
import { computed } from 'vue';
const props = defineProps({
	modelValue: Boolean,
	title: String,
	content: String,
	createdAt: [String, Number],
});
const emit = defineEmits(['update:modelValue']);

// 그래서 다음과 같이 computed를 이용
// computed는 그냥 선언하면 읽기 전용 속성이지만 setter와 getter를 사용하면 쓰기도 가능

const show = computed({
	get() {
		return props.modelValue;
	},
	set(value) {
		emit('update:modelValue', value);
	},
});

const closeModal = () => {
	show.value = false;
};
</script>

<style lang="scss" scoped></style>
