from django.shortcuts import render
from django.contrib import messages
from main.models import *
from .forms import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.contrib.messages import constants
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings



def index(request):
    
    menor_preco = Moto.objects.filter(is_visibility=True).order_by('preco')[:4]
    add_recente = Moto.objects.filter(is_visibility=True).order_by('-id')[:4]

    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        
        if form.is_valid():
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            assunto = request.POST.get('assunto')
            mensagem = request.POST.get('mensagem')
            
            conteudo = f'Nome:  {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

            print(nome, email, assunto, mensagem)

            send_mail(
                assunto, conteudo, settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER]
            )

            print("Enviado com sucesso")
            messages.add_message(request, constants.SUCCESS, 'Mensagem enviada com sucesso')
            form = ContatoForm()
        else:
            print("Erro ao enviar email")

    context = {
        'form': form,
        'menor_preco' : menor_preco,
        'add_recente' : add_recente,       
        }

    search = request.GET.get('search')

    if search:
        moto_list = Moto.objects.filter(modelo__icontains=search)
        return render(request, 'motos.html', moto_list)
    return render(request, 'index.html', context)


@login_required
def lista(request):
    motos = Moto.objects.all()

    # form = MotoForm(request.POST or None)
    # if str(request.method) == 'POST':
    #     if form.is_valid():
    #         form.save()
    #         print("Modificação feita com sucesso")

    #     else:
    #         print("Modificação falhou")
    #         form = MotoForm()
    # else:
    #     form = MotoForm() 


    context = {'motos' : motos, 
    # 'form' : form
    }
    return render(request, 'lista.html', context)

def editar_moto(request, id):
    moto = Moto.objects.get(id=id)
    return render(request, 'editar_moto.html', {'moto' : moto})

def update(request, id):
    
    modelo = request.POST.get('modelo')
    cor = request.POST.get('cor')
    ano = request.POST.get('ano')
    is_visibility = request.POST.get('is_visibility')
    
    if modelo == 'null':
        modelo = Moto.objects.get(id=id).modelo
    if cor == 'null':
        cor = Moto.objects.get(id=id).cor
    if ano == 'null':
        ano = Moto.objects.get(ano)

    if is_visibility == 'on':
        is_visibility = True
    else:
        is_visibility = False
    
    moto = Moto.objects.get(id=id)
    moto.modelo = modelo
    moto.cor = cor
    moto.ano = ano
    moto.is_visibility = is_visibility

    moto.save()
    return redirect('lista')

def logout_aplicacao(request):
    logout(request)
    return redirect('login')


def motos(request):
    
    #Inicio 
    motos = Moto.objects.filter(is_visibility=True).order_by('-id')
    
    
    cont = 0
    ate10, mais10 = False, False
    honda = False
    yamaha = False
    c100 = False
    c125 = False 
    c150 = False 
    c160 =  False 
    c250 = False 
    c300 = False

    selectform = SelectForm(request.POST or None)
    checkboxform = CheckboxForm(request.POST or None)
    
    #Ver se é um request
    if request.method == "POST":

        #Ver qual dos forms é
        if 'selectBt' in request.POST:
            if selectform.is_valid():
                print('Sucesso')
                resposta = request.POST['selecao']
                if resposta == '1':
                    motos = Moto.objects.all().order_by('-id')
                if resposta == '2':
                    motos = Moto.objects.all().order_by('-preco')
                if resposta == '3':
                    motos = Moto.objects.all().order_by('preco')
        
        if 'checkboxBt' in request.POST:
            if checkboxform.is_valid():
                if request.POST.get("ate10", False):
                    ate10 = True
                    
                if request.POST.get("mais10", False):
                    mais10 = True

                if request.POST.get("honda", False):
                    honda = True
                    
                if request.POST.get("yamaha", False):
                    yamaha = True
                
                if request.POST.get("c100", False):
                    c100 = True
                
                if request.POST.get("c125", False):
                    c125 = True

                if request.POST.get("c150", False):
                    c150 = True
                
                if request.POST.get("c160", False):
                    c160 = True

                if request.POST.get("c250", False):
                    c250 = True

                if request.POST.get("c300", False):
                    c300 = True
                
                
                vetor = [ate10, mais10, honda, yamaha, c100, c125, c150, c160, c250, c300]
                print (f'O vetor é {vetor}')

                cont = vetor.count(True)
                print(cont)
                
                ate10 = Q(preco__lte=10000) 
                mais10 = Q(preco__gte=10000)
                honda = Q(marca__icontains='honda')
                yamaha = Q(marca__icontains='yamaha')
                c100 = Q(cilindradas='100')
                c125 = Q(cilindradas='125') 
                c150 = Q(cilindradas='150') 
                c160 =  Q(cilindradas='160') 
                c250 = Q(cilindradas='250')
                c300 = Q(cilindradas='300')
                
                if cont == 1:
                    if request.POST.get("ate10", False):
                        motos = Moto.objects.all().filter(ate10)
                    
                    if request.POST.get("mais10", False):
                        motos = Moto.objects.all().filter(mais10)

                    if request.POST.get("honda", False):
                        motos = Moto.objects.all().filter(honda)

                    if request.POST.get("yamaha", False):
                        motos = Moto.objects.all().filter(yamaha)
                
                    if request.POST.get("c100", False):
                        motos = Moto.objects.all().filter(c100)
                    
                    if request.POST.get("c125", False):
                        motos = Moto.objects.all().filter(c125)

                    if request.POST.get("c150", False):
                        motos = Moto.objects.all().filter(c150)
                
                    if request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(c160)
                
                    if request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(c250)

                    if request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(c300)

                elif cont == 2:
                    print('Duas seleções')
                    
                    # Dois preços 
                    if request.POST.get("ate10", False) and request.POST.get("mais10", False):
                        motos = Moto.objects.all().filter(ate10) | Moto.objects.all().filter(mais10)


                    # Duas marcas
                    if request.POST.get("honda", False) and request.POST.get("yamaha", False):
                        motos = Moto.objects.all().filter(honda) | Moto.objects.all().filter(yamaha)

                    # Duas cilindradas
                    if request.POST.get("c100", False) and request.POST.get("c125", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c125)

                    if request.POST.get("c100", False) and request.POST.get("c150", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c150)

                    if request.POST.get("c100", False) and request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c160)

                    if request.POST.get("c100", False) and request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c250)

                    if request.POST.get("c100", False) and request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c300)



                    # Um preco e uma marca
                    if request.POST.get("ate10", False) and request.POST.get("honda", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(honda)
                    
                    if request.POST.get("ate10", False) and request.POST.get("yamaha", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(yamaha)

                    if request.POST.get("mais10", False) and request.POST.get("honda", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(honda)
                    
                    if request.POST.get("mais10", False) and request.POST.get("yamaha", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(yamaha)

                    # Um preco e uma cilindrada
                    if request.POST.get("ate10", False) and request.POST.get("c100", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(c100)
                    
                    if request.POST.get("ate10", False) and request.POST.get("c125", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(c125)
                    
                    if request.POST.get("ate10", False) and request.POST.get("c150", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(c150)
                    
                    if request.POST.get("ate10", False) and request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(c160)
                    
                    if request.POST.get("ate10", False) and request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(c250)
                    
                    if request.POST.get("ate10", False) and request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(c300)
                    
                    if request.POST.get("mais10", False) and request.POST.get("c100", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(c100)
                    
                    if request.POST.get("mais10", False) and request.POST.get("c125", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(c125)
                    
                    if request.POST.get("mais10", False) and request.POST.get("c150", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(c150)
                    
                    if request.POST.get("mais10", False) and request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(c160)
                    
                    if request.POST.get("mais10", False) and request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(c250)
                    
                    if request.POST.get("mais10", False) and request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(c300)

                    # Uma marca e uma cilindrada
                    if request.POST.get("c100", False) and request.POST.get("yamaha", False):
                        motos = Moto.objects.all().filter(c100) & Moto.objects.all().filter(yamaha)
                    
                    if request.POST.get("c125", False) and request.POST.get("yamaha", False):
                        motos = Moto.objects.all().filter(c125) & Moto.objects.all().filter(yamaha)
                    
                    if request.POST.get("c150", False) and request.POST.get("yamaha", False):
                        motos = Moto.objects.all().filter(c150) & Moto.objects.all().filter(yamaha)
                    
                    if request.POST.get("c160", False) and request.POST.get("yamaha", False):
                        motos = Moto.objects.all().filter(c160) & Moto.objects.all().filter(yamaha)
                    
                    if request.POST.get("c250", False) and request.POST.get("yamaha", False):
                        motos = Moto.objects.all().filter(c250) & Moto.objects.all().filter(yamaha)

                    if request.POST.get("c300", False) and request.POST.get("yamaha", False):
                        motos = Moto.objects.all().filter(c300) & Moto.objects.all().filter(yamaha)

                    if request.POST.get("c100", False) and request.POST.get("honda", False):
                        motos = Moto.objects.all().filter(c100) & Moto.objects.all().filter(honda)
                    
                    if request.POST.get("c125", False) and request.POST.get("honda", False):
                        motos = Moto.objects.all().filter(c125) & Moto.objects.all().filter(honda)
                    
                    if request.POST.get("c150", False) and request.POST.get("honda", False):
                        motos = Moto.objects.all().filter(c150) & Moto.objects.all().filter(honda)
                    
                    if request.POST.get("c160", False) and request.POST.get("honda", False):
                        motos = Moto.objects.all().filter(c160) & Moto.objects.all().filter(honda)
                    
                    if request.POST.get("c250", False) and request.POST.get("honda", False):
                        motos = Moto.objects.all().filter(c250) & Moto.objects.all().filter(honda)

                    if request.POST.get("c300", False) and request.POST.get("honda", False):
                        motos = Moto.objects.all().filter(c300) & Moto.objects.all().filter(honda)
               
                elif cont == 3:
                    #Três cilidradas 
                    if request.POST.get("c100", False) and request.POST.get("c125", False) and request.POST.get("c150", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c125) | Moto.objects.all().filter(c150)
                    
                    if request.POST.get("c100", False) and request.POST.get("c125", False) and request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c125) | Moto.objects.all().filter(c160)

                    if request.POST.get("c100", False) and request.POST.get("c125", False) and request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c125) | Moto.objects.all().filter(c250)
                    
                    if request.POST.get("c100", False) and request.POST.get("c125", False) and request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c125) | Moto.objects.all().filter(c300)
                    
                    if request.POST.get("c100", False) and request.POST.get("c150", False) and request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c125) | Moto.objects.all().filter(c150)

                    if request.POST.get("c100", False) and request.POST.get("c160", False) and request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c125) | Moto.objects.all().filter(c150)
                    
                    if request.POST.get("c100", False) and request.POST.get("c250", False) and request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(c100) | Moto.objects.all().filter(c125) | Moto.objects.all().filter(c150)

                    if request.POST.get("c125", False) and request.POST.get("c150", False) and request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(c125) | Moto.objects.all().filter(c150) | Moto.objects.all().filter(c160)

                    if request.POST.get("c150", False) and request.POST.get("c160", False) and request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(c150) | Moto.objects.all().filter(c160) | Moto.objects.all().filter(c250)
                    
                    if request.POST.get("c160", False) and request.POST.get("c250", False) and request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(c160) | Moto.objects.all().filter(c250) | Moto.objects.all().filter(c300)


                    # Dois precos e uma marca
                    if request.POST.get("ate10", False) and request.POST.get("mais10", False) and request.POST.get("honda", False):
                        motos = (Moto.objects.all().filter(ate10) | Moto.objects.all().filter(mais10)) & Moto.objects.all().filter(honda)
                    
                    if request.POST.get("ate10", False) and request.POST.get("mais10", False) and request.POST.get("yamaha", False):
                        motos = (Moto.objects.all().filter(ate10) | Moto.objects.all().filter(mais10)) & Moto.objects.all().filter(yamaha)

                    #Dois precos e uma cilindrada
                    if request.POST.get("ate10", False) and request.POST.get("mais10", False) and request.POST.get("c100", False):
                        motos = (Moto.objects.all().filter(ate10) | Moto.objects.all().filter(mais10)) & Moto.objects.all().filter(c100)
                    
                    if request.POST.get("ate10", False) and request.POST.get("mais10", False) and request.POST.get("c125", False):
                        motos = (Moto.objects.all().filter(ate10) | Moto.objects.all().filter(mais10)) & Moto.objects.all().filter(c125)
                    
                    if request.POST.get("ate10", False) and request.POST.get("mais10", False) and request.POST.get("c150", False):
                        motos = (Moto.objects.all().filter(ate10) | Moto.objects.all().filter(mais10)) & Moto.objects.all().filter(c150)
                    
                    if request.POST.get("ate10", False) and request.POST.get("mais10", False) and request.POST.get("c160", False):
                        motos = (Moto.objects.all().filter(ate10) | Moto.objects.all().filter(mais10)) & Moto.objects.all().filter(c160)
                    
                    if request.POST.get("ate10", False) and request.POST.get("mais10", False) and request.POST.get("c250", False):
                        motos = (Moto.objects.all().filter(ate10) | Moto.objects.all().filter(mais10)) & Moto.objects.all().filter(c250)
                    
                    if request.POST.get("ate10", False) and request.POST.get("mais10", False) and request.POST.get("c300", False):
                        motos = (Moto.objects.all().filter(ate10) | Moto.objects.all().filter(mais10)) & Moto.objects.all().filter(c300)


                    #Duas marcas e um preco 
                    if request.POST.get("honda", False) and request.POST.get("yamaha", False) and request.POST.get("ate10", False):
                        motos = (Moto.objects.all().filter(honda) | Moto.objects.all().filter(yamaha)) & Moto.objects.all().filter(ate10)
                    
                    if request.POST.get("honda", False) and request.POST.get("yamaha", False) and request.POST.get("mais10", False):
                        motos = (Moto.objects.all().filter(honda) | Moto.objects.all().filter(yamaha)) & Moto.objects.all().filter(mais10)

                    #duas marcas e uma cilindrada
                    if request.POST.get("honda", False) and request.POST.get("yamaha", False) and request.POST.get("c100", False):
                        motos = (Moto.objects.all().filter(honda) | Moto.objects.all().filter(yamaha)) & Moto.objects.all().filter(c100)
                    
                    if request.POST.get("honda", False) and request.POST.get("yamaha", False) and request.POST.get("c125", False):
                        motos = (Moto.objects.all().filter(honda) | Moto.objects.all().filter(yamaha)) & Moto.objects.all().filter(c125)
                    
                    if request.POST.get("honda", False) and request.POST.get("yamaha", False) and request.POST.get("c150", False):
                        motos = (Moto.objects.all().filter(honda) | Moto.objects.all().filter(yamaha)) & Moto.objects.all().filter(c150)
                    
                    if request.POST.get("honda", False) and request.POST.get("yamaha", False) and request.POST.get("c160", False):
                        motos = (Moto.objects.all().filter(honda) | Moto.objects.all().filter(yamaha)) & Moto.objects.all().filter(c160)
                    
                    if request.POST.get("honda", False) and request.POST.get("yamaha", False) and request.POST.get("c250", False):
                        motos = (Moto.objects.all().filter(honda) | Moto.objects.all().filter(yamaha)) & Moto.objects.all().filter(c250)
                    
                    if request.POST.get("honda", False) and request.POST.get("yamaha", False) and request.POST.get("c300", False):
                        motos = (Moto.objects.all().filter(honda) | Moto.objects.all().filter(yamaha)) & Moto.objects.all().filter(c300)


                    #Três diferentes 
                    if request.POST.get("ate10", False) and request.POST.get("honda", False) and request.POST.get("c100", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c100)
                    
                    if request.POST.get("ate10", False) and request.POST.get("honda", False) and request.POST.get("c125", False):
                        motos = (Moto.objects.all().filter(ate10) & Moto.objects.all().filter(honda)) & Moto.objects.all().filter(c125)
                    
                    if request.POST.get("ate10", False) and request.POST.get("honda", False) and request.POST.get("c150", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c150)
                    
                    if request.POST.get("ate10", False) and request.POST.get("honda", False) and request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c160)

                    if request.POST.get("ate10", False) and request.POST.get("honda", False) and request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c250)
                    
                    if request.POST.get("ate10", False) and request.POST.get("honda", False) and request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c300)
                    
                    if request.POST.get("ate10", False) and request.POST.get("yamaha", False) and request.POST.get("c125", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(yamaha) & Moto.objects.all().filter(c125)
                    
                    if request.POST.get("ate10", False) and request.POST.get("yamaha", False) and request.POST.get("c150", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(yamaha) & Moto.objects.all().filter(c150)
                    
                    if request.POST.get("ate10", False) and request.POST.get("yamaha", False) and request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(yamaha) & Moto.objects.all().filter(c160)

                    if request.POST.get("ate10", False) and request.POST.get("yamaha", False) and request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(yamaha) & Moto.objects.all().filter(c250)
                    
                    if request.POST.get("ate10", False) and request.POST.get("yamaha", False) and request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(ate10) & Moto.objects.all().filter(yamaha) & Moto.objects.all().filter(c300)
                    

                    if request.POST.get("mais10", False) and request.POST.get("honda", False) and request.POST.get("c100", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c100)
                    
                    if request.POST.get("mais10", False) and request.POST.get("honda", False) and request.POST.get("c125", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c125)
                    
                    if request.POST.get("mais10", False) and request.POST.get("honda", False) and request.POST.get("c150", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c150)
                    
                    if request.POST.get("mais10", False) and request.POST.get("honda", False) and request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c160)

                    if request.POST.get("mais10", False) and request.POST.get("honda", False) and request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c250)
                    
                    if request.POST.get("mais10", False) and request.POST.get("honda", False) and request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(honda) & Moto.objects.all().filter(c300)
                    
                    if request.POST.get("mais10", False) and request.POST.get("yamaha", False) and request.POST.get("c125", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(yamaha) & Moto.objects.all().filter(c125)
                    
                    if request.POST.get("mais10", False) and request.POST.get("yamaha", False) and request.POST.get("c150", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(yamaha) & Moto.objects.all().filter(c150)
                    
                    if request.POST.get("mais10", False) and request.POST.get("yamaha", False) and request.POST.get("c160", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(yamaha) & Moto.objects.all().filter(c160)

                    if request.POST.get("mais10", False) and request.POST.get("yamaha", False) and request.POST.get("c250", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(yamaha) & Moto.objects.all().filter(c250)
                    
                    if request.POST.get("mais10", False) and request.POST.get("yamaha", False) and request.POST.get("c300", False):
                        motos = Moto.objects.all().filter(mais10) & Moto.objects.all().filter(yamaha) & Moto.objects.all().filter(c300)


                
#PAGINAÇÃO
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '12')
    
    if not(parametro_limit.isdigit() and int(parametro_limit) > 0):
        parametro_limit = '10'

    paginator = Paginator(motos, parametro_limit)
    # trata o erro de uma paginação que não existe
    try:
        page = paginator.page(parametro_page)
    except (EmptyPage, PageNotAnInteger):
        page = paginator.page(1)


#CONTEXT
    context = {'motos' : page,
    'checkboxform' : checkboxform,
    'selectform' : selectform,
    }

#BARRA DE PESQUISA
    search = request.GET.get('search')
    if search:
        lista_filter = Moto.objects.filter(modelo__icontains=search)
        paginator = Paginator(lista_filter, parametro_limit)
        try:
            page = paginator.page(parametro_page)
        except (EmptyPage, PageNotAnInteger):
            page = paginator.page(1)
    
        cont = {'motos' : page,
        'checkboxform' : checkboxform,
        'selectform' : selectform,
        }
        return render(request, 'motos.html', cont)
    else:
        return render(request, 'motos.html', context)


def detalhes(request, id):
    moto = Moto.objects.get(id=id)
    menor_preco = Moto.objects.filter(is_visibility=True).order_by('preco')[:4]
    add_recente = Moto.objects.filter(is_visibility=True).order_by('-id')[:4]

    viewModal = False

    form = CompraForm(request.POST or None)
    
    search = request.GET.get('search') 
    if search:
        moto_list = Moto.objects.filter(modelo__icontains=search)
        return render(request, 'motos.html', moto_list)
    
    if str(request.method) == 'POST':
        
        if form.is_valid():
            nome_completo = request.POST.get('nome_completo')
            email = request.POST.get('email')
            celular = request.POST.get('celular')
            
            conteudo = f'Nome:  {nome_completo}\nE-mail: {email}\nCelular: {celular}'

            print(nome_completo, email, celular)
            moto_interessada = f'{moto.modelo} {moto.cilindradas} {moto.ano}'
            send_mail(
                'INTERESSADO NA MOTO ' + moto_interessada, conteudo, settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER]
            )
            print("Enviado com sucesso")
            viewModal = True
            form = CompraForm()
        else:
            print("Erro ao enviar email")


    context = {
        'moto' : moto,
        'form' : form,
        'menor_preco' : menor_preco,
        'add_recente' : add_recente,
        'viewModal' : viewModal, 
        }
    
    return render(request, 'detalhes.html', context)

