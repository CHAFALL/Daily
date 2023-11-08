<template>
  <div>
    {{ businessCard.name }}
    {{ businessCard.title }}
  </div>
</template>

<script setup>

const props = defineProps({
  businessCard : Object
})


</script>

<style scoped>

</style>