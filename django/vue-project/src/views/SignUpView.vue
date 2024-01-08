<template>
    <div class="box">
        <!-- <h1>회원가입하기</h1> -->
        <div class="a d-flex flex-column align-items-center p-5">
            <img src="@/assets/instagram2.png" alt="">
            <h5>친구들의 사진과 동영상을 보려면 가입하세요</h5>
            <img src="@/assets/facebook2.png" alt="">
            <div class="d-flex m-4" style="width: 100%;">
                <div style="height: 10px; width: 40%; border-bottom:1px solid black"></div>
                <p style="width: 100px;" class="text-center">또는</p>
                <div style="height: 10px; width: 40%; border-bottom:1px solid black"></div>
            </div>

            <form action="" style="width:100%" @submit.prevent="signUp">
                <input style="background-color: lightgray;" v-model="username" type="text" class="form-control" id="id" placeholder="휴대폰 번호 또는 이메일 주소">
                <br>
                <input style="background-color: lightgray;" type="text" class="form-control" id="id" placeholder="성명">
                <br>
                <input style="background-color: lightgray;" type="text" class="form-control" id="id" placeholder="사용자 이름">
                <br>
                <input style="background-color: lightgray;" v-model="password" type="password" id="inputPassword6" class="form-control" aria-describedby="passwordHelpInline" placeholder="비밀번호">
                <br>
                
                <p>저희 서비스를 이용하는 사람이 회원님의 연락처 정보를 Instagram에 업로드했을 수도 있습니다
                    더 알아보기
                </p>
                <button type="submit" class="btn btn-info" style="width: 100%;">가입</button>
            </form>
        </div>
        <br>
        <div class="a d-flex justify-content-center p-4">
            <h5>계정이 있으신가요?</h5>
            <RouterLink to="/login"><h5 style="color:blue">로그인</h5></RouterLink>
        </div>
        <div class="p-4 text-center">
            <h5>앱을 다운로드하세요</h5>
        </div>
        <div class="text-center">
        <img src="@/assets/google.png" alt="">
        </div>

    </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import {ref} from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
import router from '@/router';


const store = useCounterStore()
const username = ref(null)
const password = ref (null)


const signUp = function(){
    const payload = {
        username : username.value,
        password : password.value
    }
    store.signUp(payload)
    router.push({name:home})

}

</script>

<style scoped>
.box{
    width:500px;
    margin:auto;
}
.a{
    border:1px solid black
}
</style>