from django.shortcuts import render, redirect
from core.forms import *
from core.models import *
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'core/index.html')


class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'registration/register.html'


"""
def home(request):
    if request.POST:
        valor = request.POST['i_nome']
    else:
        valor = ''
    contexto = {'valor': valor}
    return render(request, 'core/index.html', contexto)
"""


# --------------------CLIENTE--------------------------


def cadastro_cliente(request):
    form = FormCliente(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')

    contexto = {'form': form, 'titulo': 'Cadastro de Cliente', 'stringBotao': 'Cadastrar'}
    return render(request, 'core/cadastro.html', contexto)


def lista_clientes(request):
    if request.POST:
        if request.POST['nomeCliente']:
            dados = Cliente.objects.filter(nome = request.POST['nomeCliente'])
        else:
            dados = Cliente.objects.all()
    else:
        dados = Cliente.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/lista_clientes.html', contexto)


def altera_cliente(request, id):
    objeto = Cliente.objects.get(id=id)
    form = FormCliente(request.POST or None, request.FILES or None, instance=objeto)

    if form.is_valid():
        form.save()
        contexto = {'objeto': objeto.nome, 'url': '/lista_clientes/'}
        return render(request, 'core/mensagem_salvo.html', contexto)

    contexto = {'form': form, 'titulo': 'Atualiza Cliente', 'stringBotao': 'Salvar'}
    return render(request, 'core/cadastro.html', contexto)


def exclui_cliente(request, id):
    objeto = Cliente.objects.get(id=id)
    if request.POST:
        objeto.delete()
        return redirect('url_lista_clientes')

    contexto = {'url': '/lista_clientes/', 'objeto': objeto.nome}
    return render(request, 'core/confirma_exclusao.html', contexto)


# -------------------VEICULOS----------------------------


def cadastro_veiculo(request):
    form = FormVeiculo(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')

    contexto = {'form': form, 'titulo': 'Cadastro Veiculo', 'stringBotao': 'Cadastrar'}
    return render(request, 'core/cadastro.html', contexto)


def lista_veiculos(request):
    dados = Veiculo.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/lista_veiculos.html', contexto)


def altera_veiculo(request, id):
    objeto = Veiculo.objects.get(id=id)
    form = FormVeiculo(request.POST or None, request.FILES or None, instance=objeto)

    if form.is_valid():
        form.save()
        contexto = {'objeto': objeto.modelo, 'url': '/lista_veiculos/'}
        return render(request, 'core/mensagem_salvo.html', contexto)

    contexto = {'form': form, 'titulo': 'Atualiza Veiculo', 'stringBotao': 'Salvar'}
    return render(request, 'core/cadastro.html', contexto)


def exclui_veiculo(request, id):
    objeto = Veiculo.objects.get(id=id)
    if request.POST:
        objeto.delete()
        return redirect('url_lista_veiculos')

    contexto = {'url': '/lista_veiculos/', 'objeto': objeto.modelo}
    return render(request, 'core/confirma_exclusao.html', contexto)


# --------------------FABRICANTES -------------------


def cadastro_fabricante(request):
    form = FormFabricante(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')

    contexto = {'form': form, 'titulo': 'Cadastro de Fabricante', 'stringBotao': 'Cadastrar'}
    return render(request, 'core/cadastro.html', contexto)


def lista_fabricantes(request):
    dados = Fabricante.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/lista_fabricantes.html', contexto)


def altera_fabricante(request, id):
    objeto = Fabricante.objects.get(id=id)
    form = FormFabricante(request.POST or None, request.FILES or None, instance=objeto)
    if form.is_valid():
        form.save()
        contexto = {'objeto': objeto.descricao, 'url': '/lista_fabricantes/'}
        return render(request, 'core/mensagem_salvo.html', contexto)

    contexto = {'form': form, 'titulo': 'Atualiza Fabricante', 'stringBotao': 'Salvar'}
    return render(request, 'core/cadastro.html', contexto)


def exclui_fabricante(request, id):
    objeto = Fabricante.objects.get(id=id)
    if request.POST:
        objeto.delete()
        return redirect('url_lista_fabricantes')

    contexto = {'url': '/lista_fabricantes/', 'objeto': objeto.descricao}
    return render(request, 'core/confirma_exclusao.html', contexto)


# ------------------------TABELA DE PREÇO------------------------

def tabela(request):
    dados = Tabela.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/tabela.html', contexto)


# ----------------ROTATIVOS ----------------------


def cadastro_rotativo(request):
    form = FormRotativo(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    contexto = {'form': form, 'titulo': 'Cadastro de Rotativo', 'stringBotao': 'Cadastrar', 'calendario': True}
    return render(request, 'core/cadastro.html', contexto)


def lista_rotativos(request):
    dados = Rotativo.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/lista_rotativos.html', contexto)


def altera_rotativo(request, id):
    objeto = Rotativo.objects.get(id=id)
    form = FormRotativo(request.POST or None, request.FILES or None, instance=objeto)

    if form.is_valid():
        objeto.calcula_total()
        form.save()
        contexto = {'objeto': objeto.data_entrada, 'url': '/lista_rotativos/'}
        return render(request, 'core/mensagem_salvo.html', contexto)

    contexto = {'form': form, 'titulo': 'Alterar Rotativo', 'stringBotao': 'Salvar', 'calendario': True}
    return render(request, 'core/cadastro.html', contexto)


def exclui_rotativo(request, id):
    objeto = Rotativo.objects.get(id=id)
    if request.POST:
        objeto.delete()
        return redirect('url_lista_rotativos')

    contexto = {'url': '/lista_rotativos/', 'objeto': objeto.data_entrada}
    return render(request, 'core/confirma_exclusao.html', contexto)


# ----------------- MENSALISTA -------------------


def cadastro_mensalista(request):
    form = FormMensalista(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    contexto = {'form': form, 'titulo': 'Cadastro de Mensalista', 'stringBotao': 'Cadastrar','calendario': True}
    return render(request, 'core/cadastro.html', contexto)


def lista_mensalistas(request):
    dados = Mensalista.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/lista_mensalistas.html', contexto)


def altera_mensalista(request, id):
    objeto = Mensalista.objects.get(id=id)
    form = FormMensalista(request.POST or None, request.FILES or None, instance=objeto)
    if form.is_valid():
        form.save()
        contexto = {'objeto': objeto.data_venc, 'url': '/lista_mensalistas/'}
        return render(request, 'core/mensagem_salvo.html', contexto)

    contexto = {'form': form, 'titulo': 'Altera Mensalistas', 'stringBotao': 'Salvar','calendario': True}
    return render(request, 'core/cadastro.html', contexto)


def exclui_mensalista(request, id):
    objeto = Mensalista.objects.get(id=id)
    if request.POST:
        objeto.delete()
        return redirect('url_lista_mensalistas')

    contexto = {'url': '/lista_mensalistas/', 'objeto': objeto}
    return render(request, 'core/confirma_exclusao.html', contexto)


