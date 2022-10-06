from json.encoder import INFINITY
from django.db import models

class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de atualização')

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Moto(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    valor_vista = models.DecimalField(max_digits=10, decimal_places=2)
    valor_prazo = models.DecimalField(max_digits=10, decimal_places=2)
    ano = models.IntegerField()
    cor = models.CharField(max_length=100)
    freio = models.CharField(max_length=100)
    cilindradas = models.CharField(max_length=100)
    quilometragem = models.CharField(max_length=100)
    partida = models.CharField(max_length=100)
    emplacamento = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem_principal = models.ImageField(upload_to='main/', blank=True, null=True, max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)