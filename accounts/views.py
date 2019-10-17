from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login


# Create your views here.

# 회원가입하고 로그인까지하는 것
def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # create랑 똑같음. 저장한 인스턴스반환
            user = form.save()
            auth_login(request, user)
            return redirect('todos:inde')
    else:
        form = UserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)