from django.test import TestCase
from django.utils import timezone
from members.models import Reuniao

class ReuniaoModelTest(TestCase):

    def test_criacao_de_reuniao(self):
        """
        Testa se uma instância do modelo Reuniao pode ser criada com sucesso.
        """
        print("Executando teste: test_criacao_de_reuniao") # Apenas para vermos o teste rodando

        # 1. SETUP: Criamos um objeto Reuniao no nosso banco de dados de teste
        reuniao_teste = Reuniao.objects.create(
            titulo="Reunião de Teste de Diretoria",
            data_hora=timezone.now(),
            local="Sala Virtual 1",
            tipo="RG" # Usando o valor do CHOICES ('Reunião Geral')
        )

        # 2. ASSERÇÕES: Verificamos se o objeto se comporta como o esperado
        self.assertEqual(reuniao_teste.titulo, "Reunião de Teste de Diretoria")
        self.assertEqual(reuniao_teste.get_tipo_display(), "Reunião Geral")
        self.assertTrue(isinstance(reuniao_teste, Reuniao))


    def test_metodo_str_da_reuniao(self):
        """
        Testa se o método __str__ retorna o título correto da reunião.
        """
        print("Executando teste: test_metodo_str_da_reuniao")

        # 1. SETUP
        reuniao = Reuniao.objects.create(
            titulo="Título para o Teste STR",
            data_hora=timezone.now(),
            local="Local de Teste"
        )

        # 2. ASSERÇÃO: Verificamos se a representação em string do objeto é o seu título
        self.assertEqual(str(reuniao), "Título para o Teste STR")