from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    menus = ['짜장면','짬뽕','마라탕','탕수육']
    users = ['김싸피','홍길동']
    today = datetime.datetime.today()
    context = {
        'menus' : menus,
        'users' : users,
        'today' : today,    
    }
    return render(request,'fruits/index.html',context)




def fruit(request):
    
    fruit_list = ["귤","딸기","사과","감","바나나","파인애플","구아바", "복숭아", "망고스틴"]
    hate = ["사과","구아바"]
    context = {'fruit_list': fruit_list,
               'hate':hate,}
    return render(request,'fruits/fruit.html',context)
