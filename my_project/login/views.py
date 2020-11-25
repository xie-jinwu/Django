from django.shortcuts import render
import datetime


# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        return login_result(request)


def login_result(request):
    user = request.POST.get('user')
    password = request.POST.get('password')
    now = datetime.datetime.now()
    if user == 'admin' and password == '123':
        status = '成功'
        return render(request, 'login_result.html', {'now': now, 'status': status})
    else:
        status = '失败'
        return render(request, 'login_result.html', {'now': now, 'status': status})
