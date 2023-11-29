from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

class Index(TemplateView):
    template_name = 'index.html'

class Home(TemplateView):
    template_name = 'home.html'

class Login(TemplateView):
    template_name = 'login.html'

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('index:home')  # Substitua 'nome_da_pagina_inicial' pela URL da sua página inicial
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')

    return render(request, 'login.html')  # Substitua 'login.html' pelo nome do seu template de login

from .forms import CustomUserCreationForm

def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Você criou sua conta com sucesso. Faça login para continuar.')
            return redirect('index:login')  # Substitua 'index:login' pela URL da sua view de login
    else:
        form = CustomUserCreationForm()

    return render(request, 'create_user.html', {'form': form})
