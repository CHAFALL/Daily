<template>
	<div>
		<h2>Home View</h2>
		<p>{{ $route.path }}</p>
		<p>{{ $route.name }}</p>
		<button class="btn btn-primary" @click="goAboutPage">About으로 이동</button>
		<hr class="my-4" />
		<!-- AppGrid 컴포넌트를 사용하면서 slot을 이용해 데이터를 전달 -->

		<!-- Home 컴포넌트에서는 AppGrid 컴포넌트를 사용하면서 v-slot 디렉티브를 사용하여 item 데이터를 받아 AppCard 컴포넌트에 전달합니다. 이때 AppCard 컴포넌트 내부에서는 slot을 사용하여 전달된 item 데이터를 활용할 수 있습니다. -->

		<AppGrid :items="items" v-slot="{ item }" col-class="col-3">
			<AppCard>{{ item }}</AppCard>
		</AppGrid>
	</div>
</template>

<script setup>
import AppCard from '@/components/AppCard.vue';
import AppGrid from '@/components/AppGrid.vue';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const goAboutPage = () => {
	router.push('/about');
};

const items = ref(['사과', '딸기', '포도', '바나나']);
</script>

<style lang="scss" scoped></style>
