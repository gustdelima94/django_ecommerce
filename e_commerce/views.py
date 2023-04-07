from django.shortcuts import render

from .forms import ContactForm


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
