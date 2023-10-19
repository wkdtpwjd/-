from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('index/',views.index,name='index'),   # 메인페이지 ,전체 영화데이터 조회
    path('<int:pk>/detail/',views.detail,name='detail'),         # 단일 영화데이터 조회
    # path('create/',views.create,name='create'),  # new역할
    path('create2/',views.create2,name ='create2'),
    path('<int:pk>/delete/',views.delete,name ='delete'),
    # path('<int:pk>/update/',views.update,name ='update'),  # edit 역할
    path('<int:pk>/update2/',views.update2,name ='update2'),
]
