from random import randint
from django.shortcuts import render


# no index.html ---> {% %}  --> script
def home(request):
    jogos = []
    repeticoes = []

    if request.POST:
        num = int(request.POST['numero'])
        for i in range(num):
            jogo = []
            count = 0
            while count < 5:
                x = randint(1, 20)
                if x not in jogo: #se nao ouver repeição, coloque x na lista (jogo)
                    jogo.append(x)
                    count = count + 1
            jogo.sort() # coloca em ordem crescente
            jogos.append(jogo)

        for i in range(1, 21): #1-21 para contar de 1-20
            count = 0
            for j in jogos:
                if i in j:
                    count = count + 1
            repeticoes.append(count)

    contexto = {'dados': jogos, 'repeat': repeticoes}
    return render(request, 'index.html', contexto)
