<template>
	<div class="row g-3">
		<div v-for="(item, index) in items" :key="index" :class="colClass">
			<slot :item="item" :index="index"></slot>
		</div>
	</div>
</template>

<script setup>
defineProps({
	items: {
		type: Array,
		required: true,
	},
	// 원하는 col부분에 클래스 지정해주는 법(다른 곳에서 쓸 때)
	colClass: {
		type: String,
		default: 'col-4',
	},
});
</script>

<style lang="scss" scoped></style>
