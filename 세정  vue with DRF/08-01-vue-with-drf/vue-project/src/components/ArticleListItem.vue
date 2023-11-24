<template>
  <div>
    <h5>{{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <p>{{ article }}</p>
    <RouterLink :to="{name:'DetailView',params:{id:article.id}}">
      [detail]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
defineProps({
  article:Object
})
</script>
