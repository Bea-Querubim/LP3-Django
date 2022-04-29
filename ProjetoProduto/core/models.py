from django.db import models
#admin2 - senha 123456

# principal arquivo para trabalhar com banco de dados -- cada classe será uma tabela

# função minusculo -- classe Maiusculo
# (Tabela no plural) (Objeto no singular) blank --> verifica se há informação em branco,
# null--> aceita campo em branco(nullo)


class Categoria(models.Model):
    descricao = models.CharField(max_length=50, null=False, blank=False, verbose_name='Descrição')

    def __str__(self):
        return  self.descricao

    class Meta:
        verbose_name_plural = 'Categorias'


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cnpj = models.CharField(max_length=20, verbose_name='CNPJ')
    contato_email = models.CharField(max_length=100, null=True, blank=True, verbose_name='Email')
    contato_telefone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Telefone')

    def __str__(self):
        return f'{self.nome} ({self.cnpj})'

    class Meta:
        verbose_name_plural = 'Fornecedores'


class Produto(models.Model):
    nome = models.CharField(max_length=30, verbose_name='Produto')
    valor = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Preço')
    qde_estoque = models.IntegerField(verbose_name='Quantidade em Estoque')
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    id_fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, verbose_name="Fornecedor")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Produtos'