<template>
  <div>
    <div>
      <input type="text" v-model="firstName" />
      <input type="text" v-model="lastName" />
    </div>
    <h1>{{ fullName }}</h1>
    <p>{{ title }} {{ firstName }}, {{ lastName }}</p>
    <p>{{ title }} {{ firstName }}, {{ lastName }}</p>
    <p>{{ title }} {{ firstName }}, {{ lastName }}</p>
    <div>
      <select name="" id="" v-model="selected">
        <option value="A">A</option>
        <option value="B">B</option>
        <option value="C">C</option>
      </select>
    </div>
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      firstName: 'John',
      lastName: 'Doe',
      fullName: '',
      title: 'Mr.',
      selected: '',
      changeHistory: []
    }
  },
  // 특정한 반응형 데이터를 감시를 하고 변경이 일어났을 때마다 특정 코드를 구현할 때 이용, watch에 선언되는 함수명은 감시하고픈 변수명과 동일한 것으로 해주면 된다.
  // watch로 computed와 동일한 역할을 수행도 가능
  // watch는 사용자의 데이터를 수집할 때도 이용됨(ex. 사용자가 어디에 몇 초간 머물렀는지)

  // computed는 실제 변경사항이 일어나지 않아도 이미 풀네임에 이 값들을 갖고 값이 들어가 있는 상태
  // 반면, watch는 변경이 일어나야만 그 순간에 동작
  // 즉, 미리 기존 값이 안 들어가 있다는 특징이 있다.

  watch: {
    firstName(newValue, oldValue) {
      console.log('oldValue', oldValue)
      console.log('newValue', newValue)
      this.fullName = this.title + ' ' + this.firstName + ', ' + this.lastName
    },
    lastName(newValue, oldValue) {
      console.log('oldValue', oldValue)
      console.log('newValue', newValue)
      this.fullName = this.title + ' ' + this.firstName + ', ' + this.lastName
    },
    selected(newValue, oldValue) {
      this.changeHistory.push(newValue)
      console.log(this.changeHistory)
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {}
}
</script>
