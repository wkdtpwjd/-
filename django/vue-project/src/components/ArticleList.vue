<template>
    <div>
        <h1>게시글 목록</h1>
        
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

onMounted(()=>{
    store.getArticles()
})

</script>

<style scoped>

</style>