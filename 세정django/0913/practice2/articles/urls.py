
from django.urls import path
from . import views
app_name = 'articles'

urlpatterns = [
    path('index/', views.index,name='index'),
    path('catch/<str:name>/', views.catch,name='catch'),
]