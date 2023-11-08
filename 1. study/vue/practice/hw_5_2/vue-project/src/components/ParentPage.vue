<template>
  <div class="card">
    <h1>부모 페이지 입니다.</h1>
    <ChildPage 
    v-for="child in children" 
    :key="child.name"
    :child-name="child.name"
    :child-age="child.age"
    />
  </div>
</template>

<script setup>
  
  import ChildPage from '@/components/ChildPage.vue'
  import {ref} from 'vue'

  const children = ref([
    {name:'김하나', age:30},
    {name:'김두리', age:20},
    {name:'김서이', age:10},
  ])
</script>

<style scoped>
.card{
  border : 1px solid lightgray;
  margin : 10px;
}
</style>