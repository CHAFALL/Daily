<template>
  <div>
    <h1>학생 상세 정보 목록 입니다.</h1>
    <div v-for="student in students" :key="student.name">
      <!-- <p @click="goDetail(student.name)">{{ student.name }} 학생 정보 보기</p> -->
      <RouterLink :to="{name: 'studentDetail', params: {name : student.name} }" >{{ student.name }} 학생 정보 보기</RouterLink>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router';

  const students = ref([
    {name : '김하나'},
    {name : '김두리'},
    {name : '김서이'},
  ])


  const router = useRouter()

  const goDetail = function (studentName) {
    router.push({name: 'studentDetail', params: {name : studentName} })
  }
</script>

<style scoped>

</style>