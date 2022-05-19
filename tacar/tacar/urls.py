from django.contrib import admin
from django.urls import path, include
from core.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registrar/', Registrar.as_view(), name='url_registrar'),
    path('', home, name='url_principal'),

    path('cadastro_cliente/', cadastro_cliente, name='url_cadastro_cliente'),
    path('lista_clientes/', lista_clientes, name='url_lista_clientes' ),
    path('altera_cliente/<int:id>/', altera_cliente, name='url_altera_cliente'),
    path('exclui_cliente/<int:id>/', exclui_cliente, name='url_exclui_cliente'),

    path('cadastro_veiculo/', cadastro_veiculo, name='url_cadastro_veiculo'),
    path('lista_veiculos/', lista_veiculos, name='url_lista_veiculos'),
    path('altera_veiculo/<int:id>/', altera_veiculo, name='url_altera_veiculos'),
    path('exclui_veiculo/<int:id>/', exclui_veiculo, name='url_exclui_veiculos'),

    path('cadastro_fabricante/', cadastro_fabricante, name='url_cadastro_fabricante'),
    path('lista_fabricantes/', lista_fabricantes, name='url_lista_fabricantes'),
    path('altera_fabricante/<int:id>/', altera_fabricante, name='url_altera_fabricante'),
    path('exclui_fabricante/<int:id>/', exclui_fabricante, name='url_exclui_fabricante'),

    path('cadastro_rotativo/', cadastro_rotativo, name='url_cadastro_rotativos'),
    path('lista_rotativos/', lista_rotativos, name='url_lista_rotativos'),
    path('altera_rotativos/<int:id>/', altera_rotativos, name='url_altera_rotativo'),
    path('exclui_rotativo/<int:id>/', exclui_rotativo, name='url_exclui_rotativo'),

    path('tabela/', tabela, name='url_tabela'),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

