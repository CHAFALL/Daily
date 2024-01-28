<template>
  <table class="table table-bordered table-striped">
    <thead>
      <tr>
        <th v-if="selectType === 'checkbox'">
          <input
            type="checkbox"
            class="form-check-input"
            @change="checkAll($event)"
          />
        </th>
        <th v-else-if="selectType === 'radio'"></th>
        <th :key="th.key" v-for="th in headers">
          {{ th.title }}
        </th>
      </tr>
    </thead>
    <tbody>
      <tr :key="i" v-for="(item, i) in items">
        <th v-if="selectType === 'checkbox'">
          <input
            type="checkbox"
            class="form-check-input"
            :value="item[checkedKey]"
            v-model="checkedItems"
            @change="doChecked"
          />
        </th>
        <th v-else-if="selectType === 'radio'">
          <input
            type="radio"
            class="form-check-input"
            :value="item[checkedKey]"
            v-model="checkedItem"
            @change="doChecked"
          />
        </th>
        <td :key="th.key" v-for="th in headers">{{ item[th.key] }}</td>
      </tr>
    </tbody>
  </table>
</template>
<script>
export default {
  components: {},
  props: {
    items: {
      type: Array,
      default: function () {
        return []
      }
    },
    headers: {
      type: Array,
      default: function () {
        return []
      }
    },
    selectType: {
      type: String,
      default: ''
    },
    checkedKey: {
      type: String,
      default: ''
    },
    checkedEventName: {
      type: String,
      default: 'change-item'
    }
  },
  data() {
    return {
      sampleData: '',
      checkedItems: [],
      checkedItem: ''
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {
    doChecked() {
      // console.log(this.checkedItems)
      // this.$emit('change-item', this.checkedItems)
      if (this.selectType === 'checkbox') {
        this.$emit(this.checkedEventName, this.checkedItems)
      } else if (this.selectType === 'radio') {
        this.$emit(this.checkedEventName, this.checkedItem)
      }
    },
    checkAll(event) {
      console.log(event.target.checked)
      // 얘는 위의 것과 이름만 같을 뿐 다른 것임, (함수 내에서만 이용됨)
      const checkedItems = []
      if (event.target.checked) {
        this.items.forEach((item) => {
          checkedItems.push(item[this.checkedKey])
        })
      }
      // false면 빈 배열이 할당...
      // 진또배기에 함수내에서 선언한 놈 할당
      this.checkedItems = checkedItems
    }
  }
}
</script>
