<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
    <!-- 주의사항 : parent의 메시지가 바뀌었을 때 갱신되어야 되므로 바인딩 필요(문자열이면 안된다!!) -->
    <ParentGrandChild 
    :my-msg="myMsg"
    @update-name="updateName"
    />
    <button @click="$emit('someEvent')">클릭</button>
    <button @click="buttonClick">클릭</button>
    <button @click="emitArgs">추가 인자 전달</button>
  </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue'


// 1. 문자열 배열 선언 방식
// defineProps(['myMsg'])

// 2. 객체 선언 방식 (유효성 검사에 GOOD이라 2번 방식 권장.)
// defineProps({
//   myMsg : String,
// })

// props 데이터를 script에서 사용하려면 (리턴해줘서) 반환값 받아주기
// 이렇게 사용할 일이 없다면 2번 방식으로만 해도 무관.

// const props = defineProps({
//   myMsg : String,
//   dynamicProps : String,
// })

// console.log(props)
// console.log(props.myMsg)

// 3. 다양한 객체 선언 방식
defineProps({
  myMsg : {
    type : String,
    required : true, // 값이 반드시 와야함을 의미
    // validator(value) { // 여기서의 인자는 myMsg (props)이다
    //   return ['success', 'warning', 'danger'].includes(value)
    // } 
    validator(value) {
      const validValues = ['success', 'warning', 'danger']
      if (!validValues.includes(value)) {
        console.error('에러입니다!!')
        return false
      }
      return true
    }
  }
})

// emit 선언 방식
// 위의 두 버튼은 같은 것임, 다만 차이점은 이벤트 선언을 JS에서 쓰고 사용하느냐 아니면 바로 HTML에서 사용하느냐의 차이

// 아래는 유효성을 위해서 필요, 없어도 동작은 하드라.
// prop는 필수임 근데,
const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])

const buttonClick = function () {
  emit('someEvent')
}

const emitArgs = function () {
  emit('emitArgs', 1, 2, 3)
}

const updateName = function () {
  emit('updateName')
}

</script>

<style scoped>

</style>