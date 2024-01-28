<template>
  <div>
    <input type="radio" name="" id="ai" value="AI" v-model="favoriteField" />
    <label for="ai">인공지능</label>
    <input
      type="radio"
      name=""
      id="blockchain"
      value="BC"
      v-model="favoriteField"
    />
    <label for="blockchain">블록체인</label>
    <input type="radio" name="" id="iot" value="IOT" v-model="favoriteField" />
    <label for="iot">사물인터넷</label>
    <input
      type="radio"
      name=""
      id="other"
      value="OTH"
      v-model="favoriteField"
    />
    <label for="other">기타</label>
    <div v-show="favoriteField === 'OTH'">
      <input type="text" />
    </div>
    <div v-if="favoriteField === 'OTH'">
      <input type="text" />
    </div>
  </div>
</template>
<script>
// 자주 키고 끄는 경우는 v-show를 권장, 반대는 v-if를 권장(왜냐하면 사전에 생성 되어 있지 않으므로 절약 가능, 권한 관련이 좋겠지??)
export default {
  components: {},
  data() {
    return {
      favoriteField: ''
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {}
}
</script>
