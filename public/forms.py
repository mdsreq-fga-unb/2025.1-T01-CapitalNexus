from django import forms
from django.core.validators import EmailValidator

from public.models import Projeto

class FormularioContato(forms.Form):
    nome = forms.CharField(
        max_length=100,
        label="Digite seu nome",
        widget=forms.TextInput(attrs={'placeholder': 'Bruno Silva Mars'})
    )
    email = forms.EmailField(
        label="Digite um e-mail para contato",
        widget=forms.EmailInput(attrs={'placeholder': 'mars.bruno@gmail.com'})
    )
    mensagem = forms.CharField(
        label="Digite a sua mensagem",
        widget=forms.Textarea(attrs={'placeholder': 'Olá, gostaria de formar uma parceria...'})
    )
    termos = forms.BooleanField(
        required=True,
        label="Eu li e aceito os termos de uso e a política de privacidade.",
        error_messages={'required': 'Você deve aceitar os termos para enviar a mensagem.'}
    )

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        # Inclui todos os campos do modelo no formulário
        fields = '__all__'
        widgets = {
            'resumo': forms.Textarea(attrs={'rows': 3}),
            'dimensoes': forms.Textarea(attrs={'rows': 3}),
            'situacao': forms.Textarea(attrs={'rows': 3}),
            'custo': forms.Textarea(attrs={'rows': 3}),
        }


