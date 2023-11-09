<script setup>
import MainPage from '@/components/MainPage.vue';

</script>

<template>
    <div>
      <MainPage />
      
      <RouterLink :to="{ name :'some' }">some</RouterLink>
      |
      <RouterLink :to="{ name :'other' }">other</RouterLink>
      |
      <RouterLink :to="{ name :'student' }">students</RouterLink>
      <RouterView />
    </div>


  
</template>

<style scoped>

</style>
