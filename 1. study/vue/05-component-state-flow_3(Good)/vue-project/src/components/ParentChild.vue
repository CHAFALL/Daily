<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
  </div>
  <ParentGrandChild
    :my-msg="myMsg"
    @update-name="ssafy2"
  />
  <!-- 여기서 보내주는 변수값 잘 생각하기!! -->
  <!-- 나는 지금 받는 것을 그대로 밑에 자식에게까지 보내는 중이야 -->
  
  
  <!-- 클릭되었을 때 someEvent라고 하는 이벤트가 발생했다고 막 소리를 침 -->
  <!-- 소리만 치고 처리는 부모가?? -->
  <button @click="$emit('someEvent')">클릭</button>
  <button @click="buttonClick">클릭</button>

  <button @click="emitArgs">추가 인자 전달</button>

</template>

<script setup>
  import ParentGrandChild from '@/components/ParentGrandChild.vue'


  //1.문자열 배열을 사용한 선언(prop)
  // defineProps(['myMsg'])
  //2. 객체 선언 방식(prop)
  // defineProps({
  //   myMsg : String,
  // })

  // props 데이터를 script에서 사용하려면(이걸 해줘야 인자 넘기는 것도 가능하더라...)
  const props = defineProps({
    myMsg : String,
    dynamicProps : String,
  })
  console.log(props.myMsg)

  // 3. 다양한 객체 선언 방식
  // 유효성 검사에 굳(객체 선언 방식을 쓰는 이유)
  // defineProps({
  //   myMsg: {
  //     type: String,
  //     required: true, // 반드시 값이 있어야 돼!
  //     // // 경고문만 보이기(console 창에)
  //     // validator(value) {
  //     //   return['success', 'warning', 'danger'].includes(value)
  //     // }
  //     // 아예 에러를 주자(console 창에)
  //     validator(value) {
  //       const validValues = ['success', 'warning', 'danger']
  //       if (validValues.includes(value)){
  //         console.error('에러입니다.')
  //         return false
  //       } else {
  //         return true
  //       }
  //     }
  //   }
  // })




  // emit 선언 방식(해당 방식을 좀 더 권장.)
  // 아래의 ['someEvent', 'emitArgs', 'updateName']를 지워도 정상적으로 동작
  // 아래의 emit 선언을 하는 이유? 유효성 검증을 하려고
  // 정작 필요한 것은 emit만 필요!!, 그래서 이름은 나중에 지어줘도 됨(emit 이벤트는 호출이므로)
  // 문제가 없지만 써놔라 그래도
  const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])

  //(이렇게 버튼이 클릭되었을 때 someEvent라는 이벤트가 발생했다고 소리를 치겠다라고 콜백함수를 만듬)
  // 여기서 처리하는 것이 아닌 소리를 치겠다라는 의미였네..
  const buttonClick = function () {
    emit('someEvent')
  }

  const emitArgs = function () {
    emit('emitArgs', 1, 2, 3)
  }

  const ssafy2 = function () {
  emit('updateName')
}

// emit도 객체 선언 문법으로 작성이 가능한데 emit까지 유효성 검사 할 일이 아마 없을 것이다.

</script>

<style scoped>

</style>