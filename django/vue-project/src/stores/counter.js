import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  
  const token = ref(null)
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()
  const username = ref('')
  const articles = ref([])
  
  const logIn = function(payload){
    axios({
        method:'post',
        url:'http://127.0.0.1:8000/accounts/login/',
        data :{
            username : payload.username,
            password : payload.password
        }
    })
    .then(res=>{
        console.log(res)
        console.log(res.data.key)
        token.value = res.data.key
        username.value = payload.username
      
        router.push({name:'home'})
    })
    .catch(err=>{
        console.log(err)
    })
  }

  const signUp = function(payload){
    axios({
      method : 'post',
      url: 'http://127.0.0.1:8000/accounts/registration/',
      data: {
        username : payload.username,
        password1 : payload.password,
        password2 : payload.password
      }
    })
    .then((res)=>{
      console.log('회원가입 완료')
      router.push({name:'login'})
    })
    .catch((err)=>{
      console.log(err)
    })

  }

  const getArticles = function(){
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/articles/'
    })
    .then((res)=>{
      console.log(res.data)
      articles.value = res.data
    })
    .catch((err)=>{
      console.log(err)
    })



j
  }


  return { token,logIn,signUp,username,getArticles }
})
