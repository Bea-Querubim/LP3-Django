from django.shortcuts import render, redirect
from core.forms import FormCliente, FormFabricante, FormVeiculo
from core.models import Cliente, Fabricante, Veiculo
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def home(request):
    return render(request, 'core/index.html')


class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'registration/register.html'


def cadastro_cliente(request):
    form = FormCliente(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    contexto = {'form': form,'titulo':'Cadastro de Cliente', 'stringBotao':'Cadastrar'}
    return render(request, 'core/cadastro.html', contexto)


def lista_clientes(request):
    dados = Cliente.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/lista_clientes.html', contexto)


def cadastro_veiculo(request):
    form = FormVeiculo(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    contexto = {'form': form,'titulo':'Cadastro Veiculo', 'stringBotao':'Cadastrar'}
    return render(request, 'core/cadastro.html', contexto)


def lista_veiculos(request):
    dados = Veiculo.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/lista_veiculos.html', contexto)


def cadastro_fabricante(request):
    form = FormFabricante(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    contexto = {'form': form,'titulo':'Cadastro de Fabricante', 'stringBotao':'Cadastrar'}
    return render(request, 'core/cadastro.html', contexto)


def lista_fabricantes(request):
    dados = Fabricante.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/lista_fabricantes.html', contexto)


def altera_cliente(request, id):
    objeto = Cliente.objects.get(id=id)
    form = FormCliente(request.POST or None, request.FILES or None, instance = objeto)

    if form.is_valid():
        form.save()
        contexto = {'objeto': objeto.nome, 'url':'/lista_clientes/'}
        return render(request, 'core/mensagem_salvo.html', contexto)

    contexto = {'form': form, 'titulo':'Atualiza Cliente', 'stringBotao':'Salvar'}
    return render(request, 'core/cadastro.html', contexto)


def tabela_preco(request):
    return render(request, 'core/tabela_preco.html')

def exclui_cliente(request, id):
    objeto = Cliente.objects.get(id=id)
    if request.POST:
        objeto.delete()
        return redirect('url_lista_clientes')
    contexto={'url':'/lista_clientes/', 'objeto':objeto.nome}
    return render(request, 'core/confirma_exclusao.html', contexto)