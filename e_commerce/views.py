from django.shortcuts import render


def home_page(request):
    context = {
        'title': 'O Bon Vivant',
        'content': 'Bem-vindo a página inicial!'
    }
    return render(request, 'home_Page.html', context)

def about_page(request):
    context = {
        'title': 'Sobre O Bon Vivant',
        'content': 'Bem-vindo a página sobre!'
    }
    return render(request, 'about/view.html', context)

def contact_page(request):
    context = {
        'title': 'Contato O Bon Vivant',
        'content': 'Bem-vindo a página contato!'
    }
    return render(request, 'contact/view.html', context)
