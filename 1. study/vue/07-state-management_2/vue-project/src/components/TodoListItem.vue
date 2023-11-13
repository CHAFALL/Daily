<template>
  <div>
    <!--  버튼옆에 오도록 하려고 span -->
    <span
      @click="store.updateTodo(todo.id)"
      :class="{ 'is-done' : todo.isDone }"
    >{{ todo.text }}</span>
    <button @click="store.deleteTodo(todo.id)">Delete</button>
  </div>
</template>

<script setup>
import { useTodoStore } from '@/stores/todo';
const store = useTodoStore()
const props = defineProps({
  todo : Object,
})


</script>

<style scoped>
.is-done{
  text-decoration: line-through;
}
</style>