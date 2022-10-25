from json.encoder import INFINITY
from django.db import models

class Base(models.Model):
    criado = models.DateField('Data de criação')
    modificado = models.DateField('Data de atualização: ', auto_now_add=True)
    
    def __str__(self):
        return self.criado


class Imagens(models.Model):
    imagem_sem_fundo = models.ImageField(upload_to='main/', blank=True, null=True, max_length=200)
    imagem_principal = models.ImageField(upload_to='main/', blank=True, null=True, max_length=200)
    imagem1 = models.ImageField(upload_to='main/', blank=True, null=True, max_length=200)
    imagem2 = models.ImageField(upload_to='main/', blank=True, null=True, max_length=200)
    imagem3 = models.ImageField(upload_to='main/', blank=True, null=True, max_length=200)
    imagem4 = models.ImageField(upload_to='main/', blank=True, null=True, max_length=200)
    
    def __str__(self):
        return self.imagem_principal

class Moto(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ano = models.IntegerField()
    cor = models.CharField(max_length=100)
    freio = models.CharField(max_length=100)
    cilindradas = models.CharField(max_length=100)
    quilometragem = models.CharField(max_length=100)
    partida = models.CharField(max_length=100)
    emplacamento = models.CharField(max_length=100)
    descricao = models.TextField()
    imagens = models.ForeignKey(Imagens, on_delete=models.CASCADE)
    base = models.ForeignKey(Base, on_delete=models.CASCADE)
    