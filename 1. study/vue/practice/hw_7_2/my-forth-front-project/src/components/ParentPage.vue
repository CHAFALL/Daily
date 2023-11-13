<template>
  <div class="parent">
    <h2>부모 컴포넌트</h2>
    <p>{{ family.father }}</p>
    <p>{{ family.mother }}</p>
    <ChildPage 
    v-for="child in family.children"
    :key="child.name"
    :child="child"
    />
  </div>
</template>

<script setup>
import ChildPage from '@/components/ChildPage.vue';

defineProps({
  family : Object,
})

</script>

<style scoped>
.parent{
  border: 1px solid lightgray;
  background-color: rgb(236, 232, 232);
  text-align: center;
  margin: 10px;
}
</style>