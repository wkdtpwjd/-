<template>
    <div class="container">
        <h1>로그인뷰</h1>
        <div class="d-flex">
            <div class="" style="width: 50%;">
                <img src="@/assets/instagram.png" alt="" style="width: 100%;">
            </div>
            <div style="width: 50%;">
                <div class="box d-flex flex-column align-items-center p-5">
                    <img src="@/assets/instagram2.png" alt="" style="width:70%;">
                    <form action="" style="width:100%" @submit.prevent="logIn">
                        <input v-model="username" type="text" class="form-control" id="id" placeholder="전화번호 사용자이름 또는 이메일">
                        <br>
                        <input v-model="password" type="password" id="inputPassword6" class="form-control" aria-describedby="passwordHelpInline" placeholder="비밀번호">
                        <br>
                        <button type="submit" class="btn btn-info" style="width: 100%;">로그인</button>
                    </form>
                    <div class="d-flex m-4" style="width: 100%;">
                    <div style="height: 10px; width: 80%; border-bottom:1px solid black"></div>
                    <p style="width: 100px;" class="text-center">또는</p>
                    <div style="height: 10px; width: 80%; border-bottom:1px solid black"></div>
                    </div>
                    <div class="d-flex flex-column align-items-center">
                        <img src="@/assets/facebook.png" alt="" class="mb-3">
                        <p>비밀번호를 잊으셨나요?</p>
                    </div>  
                </div>
                <div class="box text-center p-4" style="width: 100;">
                    <h4>계정이 없으신가요?<span style="color: skyblue;">가입하기</span></h4>
                </div>
                <h4 class="text-center p-4">앱을 다운로드하세요.</h4>
                <div class="text-center">
                <img src="@/assets/google.png" alt="" class="">
                </div>






            </div>
        </div>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import {ref} from 'vue'


const username = ref('')
const password = ref('')
const store = useCounterStore()

const logIn = function(){
    const payload = {
        username : username.value,
        password : password.value
    }
    store.logIn(payload)
    username.value = ''
    password.value =''
}


</script>

<style scoped>
.box {
    

    border :1px solid black
}
</style>