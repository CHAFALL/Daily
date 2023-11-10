<template>
  <div>
    <QuizCreate 
      @create-quiz="updateQuiz"
      @on-change="checkWriting"
    />
    <QuizDetail 
    v-for="quiz in quizList"
    :key="quiz.pk"
    :quiz="quiz"
    />
  </div>
</template>

<script setup>
import {ref, computed} from 'vue'
import { onBeforeRouteLeave } from 'vue-router';
import QuizDetail from '@/components/QuizDetail.vue'
import QuizCreate from '@/components/QuizCreate.vue'


const quizList = ref([
  {
    pk: 1, 
    question: 'Python 웹 프레임워크 중 하나로, 마이크로 웹 프레임워크로 빠른 개발을 지원하는 것은?', 
    answer: 'flask'
  },
  {
    pk: 2, 
    question: 'HTML에서 텍스트 입력란을 만드는 데 사용되는 요소는?', 
    answer: 'input'
  },
  {
    pk: 3, 
    question: '웹 애플리케이션에서 클라이언트의 데이터를 서버로 전송할 때 주로 사용되는 HTTP 메서드는?', 
    answer: 'post'
  },
  {
    pk: 4, 
    question: 'Python의 가상 환경을 만들어 프로젝트 별로 라이브러리 의존성을 격리시키는 명령어는?', 
    answer: 'virtualenv'
  },
  {
    pk: 5, 
    question: '웹 애플리케이션을 개발할 때, 사용자의 브라우저에 보여지는 부분을 렌더링하는 언어는 무엇인가요?', 
    answer: 'html'
  }
])

const sortedQuizList = computed(()=>{
  return quizList.value.sort((a, b) => b.pk - a.pk)
})

const updateQuiz = function(newQuiz){
  newQuiz = {
    pk: sortedQuizList.value[0].pk + 1,
    ...newQuiz,
  }
  quizList.value.push(newQuiz)
}

const isWriting = ref(false)

const checkWriting = function (newQuiz) {
  if(newQuiz.question !== '' || newQuiz.answer !== ''){
    isWriting.value = true
  } else {
    isWriting.value = false
  }
}

onBeforeRouteLeave((to, from)=>{
  if (isWriting.value){
    const ans =window.confirm('작성중이던 글이 사라집니다. 정말로 떠나실 건가요?')
    if (!ans) {
      return false
    }
  }
})
</script>

<style scoped>

</style>