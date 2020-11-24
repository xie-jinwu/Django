from django.shortcuts import render
import datetime


# Create your views here.
def login(request):
    print(request.method)
    print(request.GET)
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        print(request.method)
        print(request.POST)
        # 取到标签的name值
        user = request.POST.get('user')
        password = request.POST.get('password')
        if user == 'admin' and password == '123':
            return login_true(request)
        else:
            return login_false(request)


def login_true(request):
    now = datetime.datetime.now()
    str = "成功"
    return render(request, 'result.html', {'now': now, 'str': str})


def login_false(request):
    now = datetime.datetime.now()
    str = "失败"
    return render(request, 'result.html', {'now': now, 'str': str})
