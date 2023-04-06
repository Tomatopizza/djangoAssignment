from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib import auth
# Create your views here.
#view 
"""
장고에서 제공하는 기능을 최대한 사용해 구현해봅시다.
아래 from ... import ... 구문이 힌트입니다. 
지금은 해당 함수가 어떻게 구현되어있는지 전부다 이해 할 수는 없겠지만 
지금까지 공부한 내용으로 이해할 수 있는 부분이 있을겁니다.
모르는 부분이 있다면 지금입니다. 공부할 타이밍!
"""
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password',None)
        password2 = request.POST.get('password2',None)
        bio = request.POST.get('bio',None)

        if password != password2:
            return render(request, 'user/signup.html') #같지 않다면 signup페이지를 다시 보여줌.
        else:
            new_user = UserModel()
            new_user.username= username
            new_user.password = password
            new_user.bio = bio
            new_user.save() #데이터베이스에 저장됨.

        return redirect('/sign-in') #만약 제대로 입력되면 회원가입 페이지로 넘어감.

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        exist_user = UserModel.objects.get(username=username) #username이 같은 친구를 불러옴.
        if exist_user.password == password:
            request.session['user'] = exist_user.username
            return HttpResponse("로그인 성공")
        else:
            return redirect('/sign-in')
            # return HttpResponse("로그인 실패")
    elif request.method == 'GET':
        return render(request, 'user/signin.html')

def user_login(request):
    pass
    # 로그인 view

def user_logout(request):
    pass
    # 로그아웃 view