from django.urls import path
from main.views import *
from django.conf import settings
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', index, name='index'),
    path('motos/', motos, name='motos'),
    path('detalhes/<int:id>', detalhes, name='detalhes'),
    path('lista/', lista, name='lista'),
    path('ativacao/editar/<int:id>', editar_moto, name='editar_moto'),
    path('ativacao/update/<int:id>', update, name='update'),
    path('accounts/login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', logout_aplicacao, name='logout'),

]