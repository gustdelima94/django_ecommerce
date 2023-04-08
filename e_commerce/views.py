from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import ContactForm
from .forms import LoginForm
from .forms import RegisterForm


def home_page(request):
    context = {
        'title': 'O Bon Vivant',
        'content': 'Bem-vindo a página inicial!'
    }

    if request.user.is_authenticated:
        context['premium_content'] = 'Usuário Premium.'
    return render(request, 'home_page.html', context)

def about_page(request):
    context = {
        'title': 'Sobre O Bon Vivant',
        'content': 'Bem-vindo a página sobre!'
    }
    return render(request, 'about/view.html', context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'Contato O Bon Vivant',
        'content': 'Bem-vindo a página de contato!',
        'form': contact_form
    }
    
    # if request.method == 'POST':
    #     print(request.POST)

    if contact_form.is_valid():
        print(contact_form.cleaned_data)   
    return render(request, 'contact/view.html', context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(f'Login válido! {user}')
            return redirect('/')
        else:
            print('Login inválido!')
    return render(request, 'auth/login.html', context)

User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
            'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)   
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        new_user = User.objects.create_user(username, email, password)
        print(f'Novo usuário registrado! {new_user}')
    return render(request, 'auth/register.html', context)
