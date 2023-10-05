from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('<int:pk>/',views.detail,name='detail'),
    # create를 위한 url
    path('new/',views.new,name='new'),
    path('create/',views.create,name='create'),  # 화면을 보여주는게아니라 저장목적
]
