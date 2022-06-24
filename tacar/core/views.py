from django.shortcuts import render, redirect
from core.forms import *
from core.models import *
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


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
    try:
        form = FormCliente(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url-principal')
        contexto = {'form': form, 'titulo': 'Cadastro de Cliente', 'stringBotao': 'Cadastrar'}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)


def lista_clientes(request):
    try:
        dados = Cliente.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/lista_clientes.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)

def altera_cliente(request, id):
    try:
        objeto = Cliente.objects.get(id=id)
        form = FormCliente(request.POST or None, request.FILES or None, instance=objeto)
        if form.is_valid():
            form.save()
            contexto = {'objeto': objeto.nome, 'url': '/lista_clientes'}
            return render(request, 'core/mensagem_salvo.html', contexto)
        contexto = {'form': form,  'titulo':'Atualiza Cliente', 'stringBotao': 'Salvar'}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)


def exclui_cliente(request, id):
    try:
        objeto = Cliente.objects.get(id=id)
        if request.POST:
            object.delete()
            return redirect('url_lista_clientes')
        contexto = {'url': '/lista_clientes/', 'objeto': object.nome}
        return render(request, 'core/confirma_exclusao.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)


# -------------------VEICULOS----------------------------


def cadastro_veiculo(request):
    try:
        form = FormVeiculo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url-principal')
        else:
            contexto = {'form': form, 'titulo': 'Cadastro de Veiculo', 'stringBotao': 'Cadastrar'}
            return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)

def lista_veiculos(request):
    try:
        dados = Veiculos.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/lista_veiculos.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)

def altera_veiculo(request, id):
    try:
        objeto = Veiculos.objects.get(id=id)
        form = FormVeiculo(request.POST or None, request.FILES or None, instance=objeto)
        if form.is_valid():
            form.save()
            contexto = {'objeto': objeto.modelo, 'url': '/lista_veiculos/'}
            return render(request, 'core/mensagem_salvo.html', contexto)
        contexto = {'form': form, 'titulo': 'Atualiza Veículo', 'stringBotao': 'Salvar'}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)


def exclui_veiculo(request, id):
    try:
        objeto = Veiculos.objects.get(id=id)
        if request.POST:
            objeto.delete()
            return redirect('url_lista_veiculos')
        contexto = {'url': '/lista_veiculos/', 'objeto': objeto.modelo}
        return render(request, 'core/confirma_exclusao.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)

# --------------------FABRICANTES -------------------


def cadastro_fabricante(request):
    try:
        form = FormFabricante(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url-principal')
        else:
            contexto = {'form': form, 'titulo': 'Cadastro de Fabricante', 'stringBotao': 'Cadastrar'}
            return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)


def lista_fabricantes(request):
    try:
        dados = Fabricante.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/lista_fabricantes.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)


def altera_fabricante(request, id):
    try:
        objeto = Fabricante.objects.get(id=id)
        form = FormFabricante(request.POST or None, request.FILES or None, instance=objeto)
        if form.is_valid():
            form.save()
            contexto = {'objeto': objeto.descricao, 'url': '/lista_fabricantes/'}
            return render(request, 'core/mensagem_salvo.html', contexto)
        contexto = {'form': form, 'titulo': 'Atualiza Fabricante', 'stringBotao': 'Salvar'}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)


def exclui_fabricante(request, id):
    try:
        objeto = Fabricante.objects.get(id=id)
        if request.POST:
            objeto.delete()
            return redirect('url_lista_fabricantes')
        contexto = {'url': '/lista_fabricantes/', 'objeto': objeto.descricao}
        return render(request, 'core/confirma_exclusao.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)

# ------------------------TABELA DE PREÇO------------------------


def tabela(request):
    try:
        dados = Tabela.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/tabela.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)


# ----------------ROTATIVOS ----------------------


def cadastro_rotativo(request):
    try:
        form = FormRotativo(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('url_listagem_rotativos')
        contexto = {'form': form, 'titulo': 'Cadastro de Rotativo', 'stringBotao': 'Cadastrar', 'calendario': True}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)


def lista_rotativos(request):
    try:
        dados = Rotativo.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/listagem_rotativos.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)


def altera_rotativo(request, id):
    try:
        objeto = Rotativo.objects.get(id=id)
        form = FormRotativo(request.POST or None, instance=objeto)
        if form.is_valid():
            objeto.calcula_total()
            form.save()
            return redirect('url_listagem_rotativos')
        contexto = {'form': form, 'titulo': 'Cadastro de Rotativo', 'stringBotao': 'Cadastrar', 'calendario': True}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)


def exclui_rotativo(request, id):
    try:
        objeto = Rotativo.objects.get(id=id)
        if request.POST:
            objeto.delete()
            return redirect('url_listagem_rotativos')
        contexto = {'url': '/listagem_rotativos/', 'objeto': objeto.data_entrada}
        return render(request, 'core/confirma_exclusao.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)

# ----------------- MENSALISTA -------------------


def cadastro_mensalista(request):
    try:
        form = FormMensalista(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('url_lista_mensalista')
        contexto = {'form': form, 'titulo': 'Cadastro de Mensalista', 'stringBotao': 'Cadastrar'}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)


def lista_mensalistas(request):
    try:
        dados = Mensalista.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/lista_mensalista.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)


def altera_mensalista(request, id):
    try:
        objeto = Mensalista.objects.get(id=id)
        form = FormMensalista(request.POST or None, instance=objeto)
        if form.is_valid():
            objeto.total()
            form.save()
            return redirect('url_lista_mensalista')
        contexto = {'form': form, 'titulo': 'Cadastro de Mensalista', 'stringBotao': 'Cadastrar'}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)


def exclui_mensalista(request, id):
    try:
        objeto = Mensalista.objects.get(id=id)
        if request.POST:
            objeto.delete()
            return redirect('url_lista_mensalistas')

        contexto = {'url': '/lista_mensalistas/', 'objeto': objeto}
        return render(request, 'core/confirma_exclusao.html', contexto)
    except Exception as mensagem_erro:
        contexto2 = {'msg_erro': mensagem_erro}
        return render(request, '500.html', contexto2)

