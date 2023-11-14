import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('balance', () => {
  const balances = ref([
    {
      name: '김하나',
      balance: 100000
      },
      {
      name: '김두리',
      balance: 10000
      },
      {
      name: '김서이',
      balance: 100
      },
      
  ])

  // getter에 인자 전달
  // 게터는 내부적으로 계산된 속성일 뿐이라 파라미터를 전달할 수 없습니다. 그러나 게터에서 함수를 반환하여 모든 인자를 받을 수 있습니다

  // 리턴으로 해당 함수 값을 리턴.

  const detailInfo = computed(()=>{
    return (name) => balances.value.find((item)=>{
      return item.name === name
    })
  })

  const updateBalance = function(name) {
    balances.value = balances.value.map((item)=>{
      if(item.name===name){
        item.balance += 1000
      }
      return item
    })
  }

  return { balances, detailInfo, updateBalance }
})
