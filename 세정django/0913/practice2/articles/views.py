from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'articles/index.html')

def catch(request,name):
    # url 에서 변수로 들어오는 값을 구분해서 사용하려고 
    # 즉 캐치함수는 뒤에 문자<> 를 받아와야한다
    # 방법 : 함수에서 인자를 하나 더받는다
    print(name)
    context = {
        'name':name,
    }
    return render(request,'articles/catch.html',context)