from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from members.forms import EditarMembroForm, NovoMembroForm
from members.models import Cargo, Membro, MembroNucleo, Nucleo, Reuniao


class NovoMembroFormTest(TestCase):
    def test_email_com_dominio_invalido(self):
        form_data = {
            'username': 'novo',
            'first_name': 'Novo',
            'last_name': 'Membro',
            'email': 'teste@gmail.com',
            'password': 'senha123',
            'matricula': '123456789',
            'nucleo': None,  # Simulação sem queryset real
            'cargo': None
        }
        form = NovoMembroForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

class EditarMembroFormTest(TestCase):
    def test_email_com_dominio_invalido(self):
        form_data = {
            'nome': 'Fulano Teste',
            'email': 'invalido@gmail.com',
            'cargo': None,  # Simulação sem queryset real
            'nucleos': []
        }
        form = EditarMembroForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

class ReuniaoCreateViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='gerente', password='123')
        self.nucleo = Nucleo.objects.create(nome='Gerência')  # ou outro nome válido
        self.cargo = Cargo.objects.create(posicao='Gerente')
        self.membro = Membro.objects.create(
            user=self.user, 
            matricula="000000004", 
            nome="Teste", 
            email="teste@capitalrocketteam.com"
        )
        MembroNucleo.objects.create(membro=self.membro, nucleo=self.nucleo, cargo=self.cargo)
        
        # Fazemos o login com o cliente de teste
        self.client.login(username='gerente', password='123')
        
        # Pegamos a URL para a página de criação de reunião
        self.create_url = reverse('membros:marcar-reuniao')

    def test_criação_reuniao_com_post_sucesso(self):
        """
        Testa se uma nova reunião é criada com sucesso via POST e se o usuário é redirecionado.
        """
        print("Executando teste: test_criação_reuniao_com_post_sucesso")
        
        # 1. Verificamos quantos objetos Reuniao existem ANTES de enviar o formulário
        reunioes_antes = Reuniao.objects.count()

        # 2. Preparamos os dados do nosso formulário em um dicionário
        # As chaves ('titulo', 'data', 'hora') devem corresponder aos nomes dos campos no seu form
        data_futura = timezone.now() + timezone.timedelta(days=5)
        form_data = {
            'titulo': 'Reunião de Teste via POST',
            'data': data_futura.strftime('%Y-%m-%d'),
            'hora': data_futura.strftime('%H:%M'),
            'local': 'Sala de Testes Automatizados',
            'tipo': 'RG' # 'Reunião Geral'
        }

        # 3. Fazemos a requisição POST para a URL de criação, enviando os dados
        response = self.client.post(self.create_url, data=form_data)
        
        # 4. Asserções: Verificamos o que aconteceu depois do POST
        
        # Afirmamos que o número de reuniões no banco de dados aumentou em 1
        self.assertEqual(Reuniao.objects.count(), reunioes_antes + 1)
        
        # Afirmamos que fomos redirecionados após o sucesso (código 302)
        self.assertEqual(response.status_code, 302)
        
        # Afirmamos que fomos redirecionados para a página correta (a lista de reuniões)
        self.assertRedirects(response, reverse('membros:reunioes'))
        
        # (Opcional) Verificamos se a reunião recém-criada tem o título correto
        nova_reuniao = Reuniao.objects.latest('id')
        self.assertEqual(nova_reuniao.titulo, 'Reunião de Teste via POST')