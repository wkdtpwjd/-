<template>
    <div class="d-flex">
        <div class="a">
        <ul class="nav flex-column">
            <img src="@/assets/instagram2.png" alt="" style="width: 200px;" class="mb-4">
        <li class="nav-item">
            <div class="d-flex mb-3 bggray" style="margin-left:30px">
                <img src="@/assets/home.png" alt="" class="me-4">
                <h2 class="mt-3">홈</h2>
            </div>
        </li>
        <li class="nav-item">
            <div class="d-flex mb-3 bggray" style="margin-left:30px">
                <img src="@/assets/search.png" alt="" class="me-4">
                <h2 class="mt-3 ">검색</h2>
            </div>
        </li>
        <li class="nav-item">
            <div class="d-flex mb-3 bggray" style="margin-left:30px">
                <img src="@/assets/searchtap.png" alt="" class="me-4">
                <h2 class="mt-3">탐색 탭</h2>
            </div>
        </li>
        <li class="nav-item">
            <div class="d-flex mb-3 bggray" style="margin-left:30px">
                <img src="@/assets/lils.png" alt="" class="me-4"> 
                <h2 class="mt-3">릴스</h2>
            </div>
        </li>
        <li class="nav-item">
            <div class="d-flex mb-3 bggray" style="margin-left:30px">
                <img src="@/assets/message.png" alt="" class="me-4">
                <h2 class="mt-3">메시지</h2>
            </div>
        </li>
        <li class="nav-item">
            <div class="d-flex mb-3 bggray" style="margin-left:30px">
                <img src="@/assets/alim.png" alt="" class="me-4">
                <h2 class="mt-3">알림</h2>
            </div>
        </li>
        <li class="nav-item mb-3" style="margin-left:30px">
            <div class="d-flex bggray">
                <img src="@/assets/make.png" alt="" class="me-4">
                <h2 class="mt-3" data-bs-toggle="modal" data-bs-target="#exampleModal">만들기</h2>
            </div>
        </li>
        <li class="nav-item mb-3" style="margin-left:30px">
            <div class="d-flex bggray">
                <img src="@/assets/profile.png" alt="" class="me-4">
                <h2 class="mt-3">프로필</h2>
            </div>
        </li>
        <h5>{{ store.username }}</h5>
        </ul>

        <!--모달창-->
        <div class="modal fade modal-lg" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="d-flex">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header text-center">
                        <h1 class="modal-title fs-5 fw-bold text-center" id="exampleModalLabel">새 게시물 만들기</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div style="height: 150px;"></div>
                        <div class="text-center"><img src="@/assets/picture.png" alt=""></div>
                        <h2 class="text-center mt-4">사진과 동영상을 여기에 끌어다 놓으세요</h2>
                    </div>
                    <div class="text-center btn btn-primary" style="width:200px;margin-left: 300px;">
                        <label className="input-file-button" for="input-file">
                            컴퓨터에서 선택
                        </label>
                    
                        <input type="file" id="input-file" style="display:none"> 
                    </div>
                    <div style="height: 200px;"></div>
                </div>
            </div>
            </div>
            <div class="">

            </div>
        </div>
        <!--모달창-->

        



        </div>

        <div>
            <ArticleList/>
        </div>


    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import ArticleList from '@/components/ArticleList.vue'

const store = useCounterStore()







</script>

<style scoped>
.bggray:hover{
    background-color: lightgray;
}

.a{
    width: 350px;
    border:1px solid lightgrey
}
</style>