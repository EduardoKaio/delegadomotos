from unicodedata import name
from django import forms
from .models import *


SELECT_CHOICES = (
    ('1', 'Adicionados recentemente'),
    ('2', 'Maior preço'),
    ('3', 'Menor preço') ,
)

class SelectForm(forms.Form):
    selecao = forms.ChoiceField(required=False, choices= SELECT_CHOICES, widget=forms.Select(attrs={'class' : 'form-select form-select-sm row filtro'}), label='')

class CheckboxForm(forms.Form):
    #Preço
    ate10 = forms.BooleanField(required=False)
    mais10 = forms.BooleanField(required=False)

    #Marca
    honda = forms.BooleanField(required=False)
    yamaha = forms.BooleanField(required=False)

    #Cilindradas
    c100 = forms.BooleanField(required=False)
    c125 = forms.BooleanField(required=False)
    c150 = forms.BooleanField(required=False)
    c160 = forms.BooleanField(required=False)
    c250 = forms.BooleanField(required=False)
    c300 = forms.BooleanField(required=False)


class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, required=True, label='Nome', widget=forms.TextInput(attrs={'class' : ' input-nome'}))
    email = forms.EmailField(max_length=100, label='E-mail', widget=forms.TextInput(attrs={'class' : ' input-email', 'pattern' : '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'}))
    assunto = forms.CharField( max_length=100, label='Assunto', widget=forms.TextInput(attrs={ 'class' : ''}))
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'class' : ''}), label='Mensagem')

class CompraForm(forms.Form):
    nome_completo = forms.CharField(max_length=100,  label='', widget=forms.TextInput(attrs={'placeholder': 'Nome completo', 'class' : 'form-control nome_completo'}))
    email = forms.EmailField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'class' : 'form-control', 'pattern' : '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'}))
    celular = forms.CharField(max_length=15, label='', widget=forms.TextInput(attrs={'placeholder': 'Celular', 'class' : 'form-control','pattern' : '\([0-9]{2}\)[\s][0-9]{5}-[0-9]{4}', 'onkeypress' : 'mascara(this)', }))


class MotoForm(forms.ModelForm):
    class Meta:
        model=Moto
        fields = ['modelo', 'preco','is_visibility',]
            
        widgets = {
             'modelo': forms.TextInput(attrs={'class': 'form-control'}),
             'preco': forms.TextInput(attrs={'class': 'form-control'}),
             'is_visibility': forms.CheckboxSelectMultiple(attrs={'type': 'checkbox', 'class': ''}),
         }




