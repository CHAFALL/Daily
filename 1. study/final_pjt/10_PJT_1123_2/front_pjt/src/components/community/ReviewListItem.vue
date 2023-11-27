<template>
  <br>
  <div>

    <p>제목 : {{ review.title }}</p>
    <p>내용 : {{ review.content }}</p>
    <button @click="goToDetail" style="padding: 6px 12px; margin-bottom: 10px; background-color: #555; color: #fff; border: none; cursor: pointer; border-radius: 4px;">
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