<template>
  <div>
    <form>
      <label for="name">이름</label>
      <input type="text" id="name" v-model="name">
      <label for="title">직함</label>
      <input type="text" id="title" v-model="title">
      <button class="new-btn" @click.prevent="createCardFunc">명함 추가</button>
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  const name = ref('')
  const title = ref('')

  const emit = defineEmits(['createCardEvent'])

  const createCardFunc = function() {
    const cardInfo = {
      name: name.value,
      title: title.value,
    }
    emit('createCardEvent', cardInfo)
    name.value=''
    title.value=''
  }

</script>

<style scoped>
  .new-btn{
    padding: 10px;
    border: 1px solid blue;
    border-radius: 5px;
    background-color: white;
    color: blue;
    cursor: pointer;
  }
  .new-btn:hover{
    background-color: blue;
    color: white;
  }
</style>