<template>
	<!-- <Transition name="slide">
		<div v-if="show" class="app-alert alert" :class="typeStyle" role="alert">
			{{ message }}
		</div>
	</Transition> -->

	<div class="app-alert">
		<!-- 원래 (item, index)이런 식으로 하는데 item부분을 구조분해할당 한 것임 -->
		<TransitionGroup name="slide">
			<div
				v-for="({ message, type }, index) in items"
				:key="index"
				class="alert"
				:class="typeStyle(type)"
				role="alert"
			>
				{{ message }}
			</div>
		</TransitionGroup>
	</div>
</template>

<script setup>
// import { computed } from 'vue';

defineProps({
	items: Array,
});

// computed 불가, (왜냐하면 매개변수로 type을 받아야 하므로, 그래서 메소드로 ㄱㄱ)
const typeStyle = type => (type === 'error' ? 'alert-danger' : 'alert-primary');

// const props = defineProps({
// 	show: {
// 		type: Boolean,
// 		default: false,
// 	},
// 	message: {
// 		type: String,
// 		requierd: true,
// 	},
// 	type: {
// 		type: String,
// 		default: 'error',
// 		// success나 error가 아니면 에러
// 		validator: value => ['success', 'error'].includes(value),
// 	},
// });
// const typeStyle = computed(() =>
// 	props.type === 'error' ? 'alert-danger' : 'alert-primary',
// );
</script>

<style scoped>
.app-alert {
	position: fixed;
	top: 10px;
	right: 10px;
}
.slide-enter-from,
.slide-leave-to {
	opacity: 0;
	transform: translateY(-30px);
}
.slide-enter-active,
.slide-leave-active {
	transition: all 0.5s ease;
}
.slide-enter-to,
.slide-leave-from {
	opacity: 1;
	transform: translateY(0px);
}
</style>
