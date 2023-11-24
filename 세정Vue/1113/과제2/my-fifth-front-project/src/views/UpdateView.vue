<template>
  <div>
    <h1>데이터 수정 페이지</h1>
    <p>이름 : {{ store.balances[index].name }}</p>
    <p>잔고 : {{ store.balances[index].balance }}</p>
    <button @click="increaseBalance(store.balances[index].name)" >+</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { useBalanceStore } from '@/stores/balance'

const route = useRoute()
const index = ref(0)
const store = useBalanceStore()


const findIndex = function () {
  index.value = store.balances.findIndex((person) => person.name === route.params.name)
  console.log(index)

}
findIndex()
const increaseBalance = function (name) {
  store.updateBalance(name)
}



</script>

<style scoped>

</style>