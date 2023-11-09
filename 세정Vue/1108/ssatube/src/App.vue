<template>
  <header class="container">
    <Searchbar />
  </header>
  <main class="container">
    <div class="d-flex flex-row justify-content-between">
      <div>
        <VideoDetail 
        :video-selected="selectedVideo"/>
      </div>
      <div>
        <VideoList 
        :video-list="videoList"
        @item-select="onItemSelect"/>
      </div>
    </div>

  </main>
</template>

<script setup>
  import axios from 'axios'
  import Searchbar from '@/components/Searchbar.vue';
  import VideoList from '@/components/VideoList.vue';
  import VideoDetail from '@/components/VideoDetail.vue';

  import { ref,onMounted } from 'vue'
  const videoList = ref([
    // {id:1, title:'제목1'},
    // {id:2, title:'제목2'},
    // {id:3, title:'제목3'},
    // {id:4, title:'제목4'},
    // {id:5, title:'제목5'},
  ])
  const selectedVideo = ref(null)
  const keyword = ref('')
  const API_URL = 'https://www.googleapis.com/youtube/v3/search'
  const onItemSelect = function(video){
    // console.log('다올라왔다',video)
    selectedVideo.value = video
  }

  onMounted(()=>{
    axios({
      url:API_URL,
      params:{
        type : 'video',
        part : 'snippet',
        key : 'AIzaSyBz3_emL1SUTt_rxnuY-ybqVITXeduD53I',
        q : 'ssafy'
      }
    })
    .then((response)=>{
      console.log(response.data)
      videoList.value = response.data.items
    })
  })
  





</script>

<style scoped>

</style>