<template>
	<nav class="mt-5" aria-label="Page navigation example">
		<ul class="pagination justify-content-center">
			<li class="page-item" :class="isPrevPage">
				<a
					class="page-link"
					href="#"
					aria-label="Previous"
					@click.prevent="$emit('page', currentPage - 1)"
				>
					<span aria-hidden="true">&laquo;</span>
				</a>
			</li>
			<li
				v-for="page in pageCount"
				:key="page"
				class="page-item"
				:class="{ active: currentPage === page }"
			>
				<!-- 만족시 활성화(위) -->
				<a class="page-link" href="#" @click.prevent="$emit('page', page)">{{
					page
				}}</a>
			</li>
			<li class="page-item" :class="isNextPage">
				<a
					class="page-link"
					href="#"
					aria-label="Next"
					@click.prevent="$emit('page', currentPage + 1)"
				>
					<span aria-hidden="true">&raquo;</span>
				</a>
			</li>
		</ul>
	</nav>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
	currentPage: {
		type: Number,
		required: true,
	},
	pageCount: {
		type: Number,
		required: true,
	},
});

defineEmits(['page']);

const isPrevPage = computed(() => ({ disabled: !(props.currentPage > 1) }));
const isNextPage = computed(() => ({
	disabled: !(props.currentPage < props.pageCount),
}));
// 참고
// props이기 때문에 우리가 막 변경해선 안됨, props를 자식 컴포넌트에서 변경해야 될 경우에는 emit 이벤트를 올려줘서 부모 컴포넌트 자체에서 변경을 하도록 해야한다.
</script>

<style lang="scss" scoped></style>
