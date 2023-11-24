<template>
  <div class="center">
    <h2>부모 컴포넌트</h2>
    <p>{{ family.father }}</p>
    <p>{{ family.mother }}</p>
    <ChildPage 
    v-for="child in family.children"
    :key="child.id"
    :child="child"/>
  </div>
</template>

<script setup>
import ChildPage from '@/components/ChildPage.vue'

defineProps({
  family:Object
})
</script>

<style scoped>
.center{
  text-align: center;
  background-color: lightgray;
}
</style>
