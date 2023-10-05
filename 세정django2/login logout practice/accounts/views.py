from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout



# Create your views here.
def login(request):
    if request.method == 'POST':
        # pass  # 여기가 로그인이 이루어지는 과정 , 나중에 완성해야하는 부분
        form = AuthenticationForm(request,request.POST,)# 인자 순서가 다르다 , 두번쨰가 데이터값
        if form.is_valid():
            # 로그인 진행 (세션 데이터 생성)
            auth_login(request,form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html',context)

# createsuperuser 로 admin 계정생성하기

def logout(request):
    # 별도로 창이 필요한 게 아님
    auth_logout(request)
    return redirect('articles:index')