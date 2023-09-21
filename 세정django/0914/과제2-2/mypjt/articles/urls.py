from django.urls import path
from . import views


app_name = 'articles'  #url을 이름으로 가져다 쓸때 명확하게 구분하기 위해서 이름공간을 지정
urlpatterns = [
    path('throw/',views.throw,name = "throw"),  # 사용자가 서버로 데이터를 전달하기 위한 화면 요청 
    path('catch/',views.catch,name = "catch"),  # 사용자가 서버로 전달한 데이터를 받아서 그린 화면 응답
    # 사용자가 입력할 수 있는 화면 제공
    path('new/',views.new, name='new'),
    path('create/',views.create, name='create'),




]
