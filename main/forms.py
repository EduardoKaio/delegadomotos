from email import message
from logging import PlaceHolder
from tkinter import Widget
from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    email = forms.EmailField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Envie sua mensagem'}), label='')

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome:  {nome}\nE-mail: {email}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='E-mail enviado pelo sistema django',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio',],
            headers={'Reply-to': email}
        )
        mail.send()