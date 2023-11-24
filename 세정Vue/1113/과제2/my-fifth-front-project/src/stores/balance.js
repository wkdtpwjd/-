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

  // getters
  const updateBalance = function (name) {
    const selectBalance = computed(() => balances.value.find(balance => balance.name === name))
    selectBalance.value.balance += 1000
  }

  return { balances, updateBalance }
})
