<template>
  <div>
    <h5>{{ review.id }}</h5>
    <p>{{ review.title }}</p>
    <p>{{ review.content }}</p>
    <button @click="goToDetail" style="padding: 6px 12px; background-color: #555; color: #fff; border: none; cursor: pointer; border-radius: 4px;">
      Detail
    </button>
    <hr>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { defineProps } from 'vue';

const router = useRouter();

const props = defineProps(['review']);

const goToDetail = () => {
  router.push({ name: 'ReviewDetailView', params: { id: props.review.id } });
};
</script>