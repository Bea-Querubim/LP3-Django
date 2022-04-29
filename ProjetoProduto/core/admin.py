from django.contrib import admin
#registrar as tabelas, para abrir no admin
from  core.models import Categoria, Fornecedor, Produto

admin.site.register(Categoria)
admin.site.register(Fornecedor)
admin.site.register(Produto)


