from django.forms import ModelForm
from core.models import Cliente, Fabricante,Veiculo


class FormFabricante(ModelForm):
    class Meta:
        model = Fabricante
        fields = '__all__'


class FormCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class FormVeiculo(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'
