from django.utils import timezone
from django.test import TestCase
from django.contrib.auth.models import User 
from django.urls import reverse 
from members.models import Falta, Justificativa, Membro, Reuniao

class DashboardViewTest(TestCase):

    def setUp(self):
        """
        Este método especial é executado ANTES de cada teste nesta classe.
        É o lugar perfeito para criar objetos que serão usados em múltiplos testes.
        """
        print("Executando setUp para DashboardViewTest")
        # Criamos um usuário de teste para podermos fazer login com ele
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        # Criamos um perfil para este usuário, pois nosso dashboard pode precisar dele
        self.perfil = Membro.objects.create(user=self.user)
        # Buscamos a URL do dashboard pelo seu nome em urls.py
        self.dashboard_url = reverse('membros:reunioes')

    def test_dashboard_acessivel_para_usuario_logado(self):
        """
        Testa se um usuário logado consegue acessar o dashboard e se o template correto é usado.
        """
        print("Executando teste: test_dashboard_acessivel_para_usuario_logado")
        
        # 1. Fazemos o login com nosso cliente de teste
        self.client.login(username='testuser', password='testpassword123')
        
        # 2. Fazemos a requisição GET para a URL do dashboard
        response = self.client.get(self.dashboard_url)
        
        # 3. Asserções: Verificamos a resposta
        self.assertEqual(response.status_code, 200) # Afirmamos que a página carregou com sucesso (código 200 OK)
        self.assertTemplateUsed(response, 'members/reunioes.html') # Afirmamos que o template correto foi usado
        self.assertContains(response, "Ponto de controle") # Afirmamos que um texto específico aparece na página

    # def test_dashboard_redireciona_usuario_nao_logado(self):
    #     """
    #     Testa se um usuário NÃO logado é redirecionado para a página de login.
    #     """
    #     print("Executando teste: test_dashboard_redireciona_usuario_nao_logado")
        
    #     # 1. Fazemos a requisição GET SEM FAZER LOGIN
    #     response = self.client.get(self.dashboard_url)
        
    #     # 2. Asserções: Verificamos o redirecionamento
    #     # Afirmamos que o status da resposta é 302 (Redirecionamento)
    #     self.assertEqual(response.status_code, 302)
    #     # Afirmamos que fomos redirecionados para a página de login
    #     self.assertRedirects(response, f'/accounts/login/?next={self.dashboard_url}')

class JustificarFaltaViewTest(TestCase):
    """
    Representa uma justificativa de ausência enviada por um membro.

    A justificativa está associada a uma única instância de Falta.
    Ela inclui o texto enviado pelo membro, a data de envio, o status da análise 
    (pendente, aceita ou rejeitada), e um possível feedback da coordenação.

    A análise pode ser feita posteriormente pelo núcleo responsável.

    Campos:
        - falta (OneToOne): a falta que está sendo justificada.
        - texto_justificativa (Text): o conteúdo enviado pelo membro.
        - data_envio (DateTime): data/hora da submissão.
        - status_analise (Char): status da justificativa.
        - feedback_analise (Text): retorno da equipe (opcional).
    """

    def setUp(self):
        """
        Prepara o ambiente para os testes.
        Cria dois usuários e uma falta associada apenas ao primeiro usuário.
        """
        print("Executando setUp para JustificarFaltaViewTest")
        # Criando Usuário 1 (dono da falta)
        self.user1 = User.objects.create_user(username='membro1', password='password123')
        self.membro1 = Membro.objects.create(user=self.user1, matricula='222078893', nome='Membro Um')

        # Criando Usuário 2 (não é o dono da falta)
        self.user2 = User.objects.create_user(username='membro2', password='password123')
        self.membro2 = Membro.objects.create(user=self.user2, matricula='242078893', nome='Membro Dois')
        
        # Criando a reunião e a falta para o Membro 1
        self.reuniao = Reuniao.objects.create(titulo="Reunião para Teste de Falta", data_hora=timezone.now())
        self.falta = Falta.objects.create(reuniao=self.reuniao, membro=self.membro1)
        
        # URL dinâmica para justificar a falta do Membro 1
        self.justificar_url = reverse('membros:justificar-falta', kwargs={'falta_id': self.falta.id})

    def test_justificativa_enviada_com_sucesso(self):
        """
        Testa se o dono da falta consegue enviar uma justificativa com sucesso.
        """
        print("Executando teste: test_justificativa_enviada_com_sucesso")
        # 1. Fazemos login como o dono da falta (Membro 1)
        self.client.login(username='membro1', password='password123')
        
        # 2. Verificamos que não existe nenhuma justificativa antes
        justificativas_antes = Justificativa.objects.count()

        # 3. Preparamos os dados do formulário
        form_data = {
            'texto_justificativa': 'Tive um imprevisto e não pude comparecer.'
        }

        # 4. Enviamos a requisição POST para a URL de justificativa
        response = self.client.post(self.justificar_url, data=form_data)

        # 5. Asserções
        # Afirmamos que fomos redirecionados para a página de presenças
        self.assertRedirects(response, reverse('membros:faltaseadvertencias'))
        
        # Afirmamos que uma nova justificativa foi criada no banco de dados
        self.assertEqual(Justificativa.objects.count(), justificativas_antes + 1)
        
        # Verificamos se a justificativa foi corretamente associada à falta
        nova_justificativa = Justificativa.objects.latest('data_envio')
        self.assertEqual(nova_justificativa.falta, self.falta)
        self.assertEqual(nova_justificativa.texto_justificativa, 'Tive um imprevisto e não pude comparecer.')

    def test_usuario_nao_pode_justificar_falta_de_outro(self):
        """
        Testa se um usuário não consegue nem acessar a lógica de justificar a falta de outro membro.
        """
        print("Executando teste: test_usuario_nao_pode_justificar_falta_de_outro")
        # 1. Fazemos login como o usuário "intruso" (Membro 2)
        self.client.login(username='membro2', password='password123')
        
        # 2. Preparamos dados de formulário
        form_data = {'texto_justificativa': 'Tentando justificar a falta de outra pessoa.'}

        # 3. Tentamos enviar um POST para a URL da falta do MEMBRO 1
        response = self.client.post(self.justificar_url, data=form_data)

        # 4. Asserção
        # Afirmamos que a página retornou um erro 404 - Não Encontrado.
        # Isso prova que a linha get_object_or_404(..., membro__user=request.user) funcionou,
        # pois não encontrou uma falta para o usuário logado com aquele ID.
        self.assertEqual(response.status_code, 404)