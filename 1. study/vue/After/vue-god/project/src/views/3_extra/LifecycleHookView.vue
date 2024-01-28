<template>
  <div>
    <div>{{ sampleData }}</div>
    <div>
      <label for="">태어난 도시는?</label>
      <select name="" id="">
        <option value="" :key="city.code" v-for="city in cities">
          {{ city.title }}
        </option>
      </select>
    </div>
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      sampleData: '',
      cities: [],
      fnInterval: null
    }
  },

  setup() {},
  // beforeCreate: 인스턴스가 초기화되면 props 설정을 처리한 후 data() 또는 computed 같은 다른 옵션을 처리하기 직전에 호출이 된다.
  beforeCreate() {},
  // created: data(), watch, computed, methods 이런 정보를 모두 가지고 준비가 끝난 상태

  created() {
    this.getCityList()
  },
  // beforeMount: 반응 상태 설정을 완료를 했지만, 아직 DOM 노드가 생성되지 않은 상태
  beforeMount() {},
  // mounted: 실제 DOM이 렌더링이 끝난 상태
  mounted() {
    // this.getCityList()
    // setInterval: 특정 지정된 시간마다 계속해서 특정 함수를 호출
    this.fnInterval = window.setInterval(() => {
      console.log('aaaa')
    }, 1000)
  },
  // beforeUpdate: data 변경으로 인해 DOM을 업데이트하기 직전 상태
  beforeUpdate() {},
  // updated: DOM이 업데이트 된 후에 호출
  updated() {},
  // beforeUnmount: 현재 컴포넌트를 빠져 나가기 직전
  beforeUnmount() {},
  // unmounted: 현재 컴포넌트를 빠져 나갈 때
  unmounted() {
    window.clearInterval(this.fnInterval)
    this.fnInterval = null
    this.cities = null
  },
  methods: {
    getCityList() {
      // 서버에 도시 목록을 요청한 것으로 가정
      // 가져오는데 시간이 소요
      this.cities = [{ code: '02', title: '서울' }]
    }
  }
}

// 참고?: created와 mounted에서 데이터를 갖고 오는 부분들을 적절하게 분리를 하면 되게 효율적으로 할 수 있다.
// 그렇다고 created부분에 다 때려 박는다?? - 양이 많으면 오랫동안 하얀색 바탕만 사용자가 보고 있을 수 있다.

// created부분은 사용자가 이 화면을 접속하자마자 가장 먼저 봐야되는 데이터와 관련되어 있는 그런 함수들 그런 애들을 이 시점에 호출함
// ex) 표는 덜 만들어졌지만 표 속의 값은 보이게, 또는 휠의 윗 부분
</script>
