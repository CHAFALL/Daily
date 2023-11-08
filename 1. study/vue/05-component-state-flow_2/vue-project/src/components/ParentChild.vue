<template>
  <div>
    <h5>ParentChild</h5>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
    <!-- 얘는 바로 쏴준 느낌 -->
    <button @click="$emit('someEvent')">클릭</button>
    <button @click="emitArgs">추가 인자 전달</button>
    <ParentGrandChild 
      :my-msg="myMsg"
      :dynamic-props="dynamicProps"

      @update-name="updateName"      
    />
    <!-- 이벤트를 받아서 단순히 올려주는 역할? -->
  </div>
</template>

<script setup>

import ParentGrandChild from '@/components/ParentGrandChild.vue'

// props
const props = defineProps({
  myMsg : String,
  dynamicProps : String,
})

console.log(props)
console.log(props.myMsg)

//emit
const emit = defineEmits(['someEvent','emitArgs', 'updateName'])

const emitArgs = function () {
  emit('emitArgs', 1, 2, 3)
}


const updateName = function () {
  emit('updateName')
}

</script>

<style scoped>

</style>