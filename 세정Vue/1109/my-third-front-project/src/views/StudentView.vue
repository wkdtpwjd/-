<template>
  <div>
    <h1>학생 상세 정보 목록 입니다.</h1>
    <p v-for="i in students"
    @click="detailpage(i.name)">{{i.name}} 학생 정보 보기</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import {useRoute,useRouter,onBeforeRouteLeave,onBeforeRouteUpdate} from 'vue-router'

const router = useRouter()

const students = ref([
  {name:'김하나'},
  {name:'김두리'},
  {name:'김서이'}
])

const detailpage = function(name){
  router.push({name:'studentdetail',params:{studentname:name}})
}

</script>

<style scoped>

</style>