<template>
  <div>
    <button @click="changeValue" ref="btn">변경</button>
    <!-- 바인딩이 없으면 문자로만 인식!! -->
    <ChildComponent
      :str="strParent"
      :num="numParent"
      :isOk="isOkParent"
      :arr="arrParent"
      :obj="objParent"
      @change-num="getData"
      ref="child1"
    />
    <!-- ref는 vue에서 쓰는 html 태그의 id와 같은 것(유일한 값만 가능) -->
    <!-- 또한 ref는 html 속성처럼 어떤 html 요소에도 다 넣을 수 있음 -->
    <!-- 그냥 vue에서 html id와 기능이 같다고 보면 됨 -->
  </div>
</template>
<script>
import ChildComponent from '@/components/fragments/ChildComponent.vue'
export default {
  components: { ChildComponent },
  data() {
    return {
      sampleData: '',
      strParent: 'CHAFA',
      numParent: 12,
      isOkParent: true,
      arrParent: [1, 2, 3, 4, 5],
      objParent: { name: 'Jeremy' }
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {
    getData(data) {
      console.log('자식 컴포넌트에서 이벤트 호출')
      console.log(data)
    },
    changeValue() {
      // 아래와 같이 하면 해당 부분에 접근 가능!!
      this.$refs.child1.str2 = 'Seoul'
      this.$refs.child1.printMessage()
    }
  }
}
// 이렇게 부모에서 자식 컴포넌트에 정의되어 잇는 데이터를 부모에서 자식 컴포넌트로 Propose를 이용해서 데이터를 전달할 수도 있고 자식 컴포넌트에 사용하고 있는 데이터를 직접적으로(ref) 접근해서 바꿀 수 있다!!
</script>
