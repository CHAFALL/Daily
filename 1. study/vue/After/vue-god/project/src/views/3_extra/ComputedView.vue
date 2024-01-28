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
    <p>{{ fullName }}</p>
    <div>
      <label for="age">당신의 나이는?</label>
      <input type="number" name="" id="age" v-model="age" />
    </div>
    <p>{{ age >= 20 ? '성인' : '미성년자' }}</p>
    <p>{{ isAdult }}</p>
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      firstName: 'John',
      lastName: 'Doe',
      title: 'Mr.',
      age: 0
    }
  },
  // 반응형으로 연결된 것들이 바뀔 때 알아서 연산되어줌(여러곳에서 보여져야 한다면 이용됨!!)
  computed: {
    fullName() {
      return this.title + ' ' + this.firstName + ', ' + this.lastName
    },
    isAdult() {
      return this.age >= 20 ? '성인' : '미성년자'
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {}
}
</script>
