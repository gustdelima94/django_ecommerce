from django import forms
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    full_name = forms.CharField(
            label='Nome completo',
            error_messages={'required': 'Nome inválido!'},
            widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Informe o nome completo"
            }
        )
    )
                
    email = forms.EmailField(
            label='E-mail',
            error_messages={'invalid': 'E-mail inválido!'},
            widget=forms.EmailInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Informe o e-mail"
            }
        )
    )

    message = forms.CharField(
            label='Mensagem',
            error_messages={'required': 'Mensagem inválida!'},
            widget=forms.Textarea(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Informe a mensagem"
            }
        )
    )


class RegisterForm(forms.Form):
    username = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Esse usuário já existe. Informe outro usuário.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Esse e-mail já existe. Informe outro e-mail.')
        return email
    
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('As senhas não coincidem. Informe senhas iguais.')
        return data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
