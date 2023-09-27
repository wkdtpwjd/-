from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

# 인덱스 화면
def index(request):
    return render(request,'articles/index.html')


def select(request):
    return render(request,'articles/select.html')