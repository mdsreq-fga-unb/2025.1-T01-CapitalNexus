from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from members.models import Membro, Reuniao


class ReuniaoCreateViewTest(TestCase):

    def setUp(self):
        """Prepara o ambiente para os testes de criação de reunião."""
        print("Executando setUp para ReuniaoCreateViewTest")
        # Criamos um usuário de teste
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        # Criamos o perfil para ele
        Membro.objects.create(user=self.user)
        
        # Fazemos o login com o cliente de teste
        self.client.login(username='testuser', password='testpassword123')
        
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