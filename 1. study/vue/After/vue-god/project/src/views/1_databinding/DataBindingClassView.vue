<template>
  <div>
    <!-- 참고로 한 단어이면 클래스 명에 '' 안해줘도 됨 -->
    <div :class="{ 'text-red': hasError, active: isActive }">클래스 바인딩</div>
    <!-- 배열 형태는 실제로 그렇게 많이 이용 x -->
    <div :class="class2">클래스 바인딩2</div>
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      isActive: false,
      hasError: false,
      class2: ['active', 'text-red']
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {}
}
</script>
<style scoped>
.active {
  background-color: greenyellow;
  font-weight: bold;
}

.text-red {
  color: red;
}
</style>
