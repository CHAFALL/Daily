<template>
  <div>
    <div>
      <input
        type="checkbox"
        name=""
        id="html"
        value="HTML"
        v-model="favoriteLang"
      />
      <label for="html">HTML</label>
    </div>
    <div>
      <input
        type="checkbox"
        name=""
        id="css"
        value="CSS"
        v-model="favoriteLang"
      />
      <label for="css">CSS</label>
    </div>
    <div>
      <input
        type="checkbox"
        name=""
        id="js"
        value="JS"
        v-model="favoriteLang"
      />
      <label for="js">JavaScript</label>
    </div>
    <div>선택한 지역:{{ favoriteLang }}</div>
  </div>
  <!-- 원래는 name을 동일시 해서 체크박스를 묶어줬는데 v-model(배열)을 통해서 하나의 그룹으로 묶을 수 있음 -->
  <!-- 주의사항: checkbox는 특이하게 v-model로 양방향을 했지만 value와 연결이 되어있는 것이 아니라 checked라는 속성하고 연결이 되어있다. -->
</template>
<script>
export default {
  components: {},
  data() {
    return {
      favoriteLang: []
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {}
}
</script>
