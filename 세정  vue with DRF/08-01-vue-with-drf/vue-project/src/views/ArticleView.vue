<template>
  <div>
    <h1>Article page</h1>
    <RouterLink :to="{name: 'CreateView'}">
      [create]
    </RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import ArticleList from '@/components/ArticleList.vue'
import { RouterLink } from 'vue-router';

const store = useCounterStore()

onMounted(()=>{
  store.getArticles()
})


</script>

<style>

</style>
