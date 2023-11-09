<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
    <ParentsGrandChild :my-msg="myMsg"
    @update-name="updateName"/>
    <button @click="$emit('someEvent')">클릭</button>
    <button @click="buttonClick">클릭</button>
    <button @click="emitArgs">추가 인자 전달</button>
  </div>
</template>

<script setup>
import ParentsGrandChild from '@/components/ParentsGrandChild.vue'
// defineProps(['myMsg'])
// defineProps({
//   myMsg: String,
// })

//props데이터를 script에서 사용하려면 
const props = defineProps({
  myMsg: String,
  dynamicProps:String,
})

console.log(props.myMsg)


// emit 선언 방식
const emit = defineEmits(['someEvent','emitArgs','updateName'])

const buttonClick = function(){
  emit('someEvent')
}

const emitArgs = function(){
  emit('emitArgs',1,2,3)
}

const updateName = function(){
  emit('updateName')
}


// 다양한 객체 선언 방식
// defineProps({
//   myMsg:{
//     type:String,
//     required:true,
//   }
// })






</script>

<style  scoped>

</style>