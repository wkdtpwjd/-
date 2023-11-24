<template>
  <div>
    <p>이름 : {{ balance.name  }}</p>
    <p>잔고 : {{ balance.balance }}</p>
    <button @click="goUpdate">updateBalance</button>
    <hr>
  </div>
</template>

<script setup>
import { useRouter} from 'vue-router'

const router = useRouter()

const props = defineProps({
  balance:Object
})

const goUpdate = function(){
  router.push({name:'update', params:{name: props.balance.name}})
  // console.log(props.balance.name)
}
</script>

<style scoped>

</style>