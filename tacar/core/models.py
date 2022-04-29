from django.db import models


# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    foto = models.ImageField(upload_to='fotos_clientes', blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Clientes'


class Fabricante(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = 'Fabricantes'


class Veiculo(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField(default=2022, blank=True, null=True)
    cor = models.CharField(max_length=30, blank=True, null=True)
    placa = models.CharField(max_length=10)
    foto = models.ImageField(upload_to='fotos_veiculos', blank=True, null=True)

    def __str__(self):
        return f'{self.placa} ({self.modelo})'

    class Meta:
        verbose_name_plural = 'Veículos'


class Tabela(models.Model):
    descricao = models.CharField(max_length=50, verbose_name="Descricao")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")

    def __str__(self):
        return f'{self.descricao} - {self.valor}'

    class Meta:
        verbose_name_plural = 'Tabelas'


class Mensalista(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    id_tabela = models.ForeignKey(Tabela, on_delete=models.CASCADE, verbose_name="Tarifa")
    data_venc = models.IntegerField(default=5, verbose_name="Dia Vencimento")
    em_pendencia = models.BooleanField(default=False, blank=True, null=True, verbose_name="Devedor")

    def __str__(self):
        return f'{self.id_cliente} - {self.id_tabela}'


    class Meta:
        verbose_name_plural = 'Mensalistas'


class Rotativo(models.Model):
    id_veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name="Veiculo")
    id_tabela = models.ForeignKey(Tabela, on_delete=models.CASCADE, verbose_name="Tabela")
    data_entrada = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="Entrada")
    data_saida = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name="Saida")
    pago = models.BooleanField(default=False, blank=False, null=False, verbose_name="Status Pagamento")
    total = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2, verbose_name="Total")

    def __str__(self):
        return f'{self.id_veiculo} - {self.data_entrada}'

    class Meta:
        verbose_name_plural = 'Rotativos'

