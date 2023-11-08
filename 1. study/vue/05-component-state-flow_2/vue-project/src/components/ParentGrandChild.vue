<template>
  <div>
    <h5>ParentGrandChild</h5>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
    <button @click="updateName">이름 변경</button>
  </div>
</template>

<script setup>

const props = defineProps({
  myMsg : String,
  dynamicProps : String,
})

const emit = defineEmits(['updateName'])


const updateName = function() {
  //emit 상위로 보내야 한다. // 여기서 보내는 거구나
  emit('updateName')
}


</script>

<style scoped>

</style>