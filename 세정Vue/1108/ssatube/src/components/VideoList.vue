<template>
  <div>
    <h1>여기는 리스트</h1>
    <ul>
      <VideoListItem v-for="video of videoList" 
      :key="video.id"
      :video="video"
      @item-select="onItemSelect"/>
    </ul>
  </div>
</template>

<script setup>
import VideoListItem from '@/components/VideoListItem.vue';
  defineProps(
    {videoList:Array}
  )
  const emit = defineEmits(['itemSelect'])
  const onItemSelect = function(video){
    // console.log('아이템이 선택되었습니다')
    // console.log(video)
    emit('itemSelect',video)
  }
</script>

<style scoped>

</style>