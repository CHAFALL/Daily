import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  let id = 0
  const todos = ref([
    {id: id++, text: '할 일 1', isDone: false},
    {id: id++, text: '할 일 2', isDone: false},
  ])

  const addTodo = function (todoText) {
    todos.value.push({
      id : id++,
      text: todoText,
      isDone : false
    })
  }

  const deleteTodo = function (todoId) {
    const index = todos.value.findIndex((todo)=>{
      return todo.id === todoId
    })
    todos.value.splice(index, 1) // 해당 인덱스부터 1개 삭제
  }

  const updateTodo = function (todoId) {
    todos.value = todos.value.map((todo)=>{
      if (todo.id === todoId) {
        todo.isDone = !todo.isDone
      }
      return todo //map이니깐.
    })
  }

  const doneTodosCount = computed(()=>{
    return todos.value.filter((todo)=> todo.isDone).length
  })

  // 그냥 가지고 논 것임.
  // const findTodo = computed((todoId)=>{
  //   return todos.value.find((todo)=> todo.id === todoId)
  // })


  return { todos, addTodo, deleteTodo, updateTodo, doneTodosCount}
}, {persist : true})
