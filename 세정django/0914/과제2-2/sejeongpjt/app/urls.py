from django.urls import path
from . import views
app_name = 'app'
urlpatterns = [
    path('throw/',views.throw,name="throw"),
    path('catch/',views.catch,name="catch"),
    path('new/',views.new,name="new"),
    path('store/',views.store,name="store"),
]