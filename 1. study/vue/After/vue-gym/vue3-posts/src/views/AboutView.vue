<template>
	<div>
		<h2>About View</h2>
		<p>{{ $route.path }}</p>
		<p>{{ $route.name }}</p>
		<button class="btn btn-primary" @click="$router.push('/')">
			Home으로 이동
		</button>
		<h2>Store</h2>
		<p>counter: {{ store.counter }}</p>
		<p>counter2: {{ counter }}</p>
		<p>doubleCount: {{ doubleCount }}</p>
		<p>doubleCountPlusOne: {{ doubleCountPlusOne }}</p>
		<button @click="increment()">Click!!</button>
	</div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
import { storeToRefs } from 'pinia';

const route = useRoute();
console.log('route.path: ', route.path);

const store = useCounterStore();
// store는 reactive로 매핑된 객체임을 알 수 있다.
// 즉, 구조분해 할당을 한다면 반응성 연결이 끊어지겠지!!
// 이를 위한 함수가 존재!! -> storeToRefs
// console.log(store);

const { counter, doubleCount, doubleCountPlusOne } = storeToRefs(store);
counter.value = 100;

// actions는 그냥 구조분해할당 바로 박아버려도 됨
const { increment } = store;
</script>

<style lang="scss" scoped></style>
