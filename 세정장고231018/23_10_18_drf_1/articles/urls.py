from django.urls import path
from articles import views
# api/v1/articles/
# api/v1/articles/<pk>/
urlpatterns = [
    # 게시글 목록 조회, 게시글 작성
    path('articles/', views.article_list),
    
    # 게시글 조회, 수정, 삭제   RUD
    path('articles/<int:article_pk>/', views.article_detail),
]
