from django.shortcuts import render # render = renderiza o template  (1 - caminho quando tem o template)
from django.http import HttpResponse # (2  - caminho dirto sem o template)
import random
# view como se fosse o controller (mvc) -e- template como se fosse o view (mvc)

def home (request):
    num = random.randint (0,20)
    page = f'<body> Hello Little Padawan :3  <p> Teste: numero aleatorio {num} </p</body>'
    return HttpResponse(page)