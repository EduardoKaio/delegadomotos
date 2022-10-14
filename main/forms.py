from ast import pattern
from email import message
from logging import PlaceHolder
from tkinter import Widget
from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, required=True, error_messages={'required': 'joga e joga'}, label='Nome', widget=forms.TextInput(attrs={'class' : ' input-nome'}))
    email = forms.EmailField(max_length=100, label='E-mail', widget=forms.TextInput(attrs={'class' : ' input-email', 'pattern' : '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'}))
    assunto = forms.CharField( max_length=100, label='Assunto', widget=forms.TextInput(attrs={ 'class' : ''}))
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'class' : ''}), label='Mensagem')

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome:  {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio',],
            headers={'Reply-to': email}
        )
        mail.send()

class CompraForm(forms.Form):
    nome_completo = forms.CharField(max_length=100,  label='', widget=forms.TextInput(attrs={'placeholder': 'Nome completo', 'class' : 'form-control nome_completo'}))
    email = forms.EmailField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'class' : 'form-control', 'pattern' : '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'}))
    celular = forms.CharField(max_length=15, label='', widget=forms.TextInput(attrs={'placeholder': 'Celular', 'class' : 'form-control', 'onkeypress' : 'mascara(this)', }))

    def send_mail(self):
        nome_completo = self.cleaned_data['nome_completo']
        email = self.cleaned_data['email']
        celular = self.cleaned_data['celular']

        conteudo = f'Nome Completo: {nome_completo}\nE-mail: {email}\nCelular: {celular}'

        mail = EmailMessage(
            subject='E-mail enviado a respeito da moto',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio',],
            headers={'Reply-to': email}
        )
        mail.send()