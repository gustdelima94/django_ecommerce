from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(
        error_messages={'required': 'Nome inválido!'},
        widget=forms.TextInput(
            attrs={
                "class": "form-control", 
                "placeholder": "Informe o nome completo."
            }
        )
    )
                
    email = forms.EmailField(
        error_messages={'invalid': 'E-mail inválido!'},
        widget=forms.EmailInput(
            attrs={
                "class": "form-control", 
                "placeholder": "Informe o e-mail."
            }
        )
    )

    message = forms.CharField(
        error_messages={'required': 'Mensagem inválida!'},
        widget=forms.Textarea(
            attrs={
                "class": "form-control", 
                "placeholder": "Informe a mensagem."
            }
        )
    )
