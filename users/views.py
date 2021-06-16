from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        # Register User
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Такое имя пользователя уже существует.')
                return redirect('users:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Пользователь с таким имейлом уже существует.')
                    return redirect('users:register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name, last_name=last_name)
                    auth.login(request, user)
                    return redirect('home:index')

        else:
            messages.error(request, 'Пароли не совпадают.')
            return redirect('users:register')
        return redirect('users:register')

    return render(request, 'users/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('home:index')
        else:
            messages.error(request, 'Такого пользователя не существует.')
        return redirect('users:login')
    return render(request, 'users/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home:index')
