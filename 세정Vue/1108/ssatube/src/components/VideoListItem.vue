<template>
  <li @click="onClick">
    <!-- <p>id : {{ video.id }}</p>
    <p>title :{{ video.title }}</p> -->
    <img :src="video.snippet.thumbnails.default.url" alt="">
    <p>{{ video.snippet.title }}</p>
  </li>
</template>

<script setup>
const emit = defineEmits(['itemSelect'])
const props = defineProps ({
  video:Object
})

const onClick = function() {
  emit('itemSelect',props.video)
}
</script>

<style scoped>

</style>