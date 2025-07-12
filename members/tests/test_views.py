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
class AvaliarJustificativasTest(TestCase):
    """
    Conjunto de testes para a funcionalidade de avaliação de justificativas.
    """
    def setUp(self):
        """
        Prepara o ambiente inicial para todos os testes desta classe.

        Cria um gestor, um membro comum, uma reunião, uma falta para o membro
        e uma justificativa pendente para essa falta.

        Args:
            None

        Returns:
            None
        """
        print("Executando setUp para AvaliarJustificativasTest")

        # 2. Criar usuário gestor e seu perfil de membro
        self.gestor_user = User.objects.create_user('gestor', 'gestor@capitalrocketteam.com', 'password')
        self.gestor_membro = Membro.objects.create(user=self.gestor_user, matricula='231020220', nome='Gestor Teste')
        
        # 3. Criar usuário membro comum e seu perfil
        self.membro_user = User.objects.create_user('membro', 'membro@capitalrocketteam.com', 'password')
        self.membro_comum = Membro.objects.create(user=self.membro_user, matricula='200012345', nome='Membro Comum')

        # 4. Criar dados para a justificativa
        self.reuniao = Reuniao.objects.create(titulo="Reunião de Teste", data_hora=timezone.now())
        self.falta = Falta.objects.create(reuniao=self.reuniao, membro=self.membro_comum)
        self.justificativa = Justificativa.objects.create(falta=self.falta, texto_justificativa="Justificativa de teste.")

        # 5. URLs que serão usadas nos testes
        self.url_lista = reverse('membros:justificativas')
        self.url_processar = reverse('membros:processar', kwargs={'just_id': self.justificativa.id})

    def test_gestor_pode_ver_pagina_de_avaliacao(self):
        """
        Testa se um usuário gestor consegue acessar a página de avaliação de justificativas.

        Args:
            None

        Returns:
            None
        """
        print("Executando teste: test_gestor_pode_ver_pagina_de_avaliacao")
        self.client.login(username='gestor', password='password')
        response = self.client.get(self.url_lista)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'members/justificativas.html')
        self.assertContains(response, self.justificativa.texto_justificativa) # Verifica se a justificativa pendente aparece

    # def test_membro_comum_nao_pode_ver_pagina_de_avaliacao(self):
    #     """
    #     Testa se um membro comum é redirecionado ao tentar acessar a página de avaliação.

    #     Args:
    #         None

    #     Returns:
    #         None
    #     """
    #     print("Executando teste: test_membro_comum_nao_pode_ver_pagina_de_avaliacao")
    #     # NOTA: Este teste espera que a verificação 'is_gestor' na sua view esteja ativa (não comentada)
    #     self.client.login(username='membro', password='password')
    #     response = self.client.get(self.url_lista)
        
    #     # Esperamos um redirecionamento (código 302)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, reverse('dashboard')) # Verifica se redirecionou para o dashboard

    def test_gestor_pode_aprovar_justificativa(self):
        """
        Testa se um gestor pode aprovar uma justificativa com sucesso via POST.

        Args:
            None

        Returns:
            None
        """
        print("Executando teste: test_gestor_pode_aprovar_justificativa")
        self.client.login(username='gestor', password='password')
        
        # Dados que seriam enviados pelo formulário da modal
        post_data = {
            'decisao': 'ACEITA',
            'feedback_analise': 'Justificativa aceita pela gestão.'
        }

        response = self.client.post(self.url_processar, data=post_data)

        # Verifica o redirecionamento
        self.assertRedirects(response, self.url_lista)

        # Busca a justificativa no banco de dados novamente para verificar se ela foi alterada
        self.justificativa.refresh_from_db()

        # Afirma que o status foi realmente alterado para 'ACEITA'
        self.assertEqual(self.justificativa.status_analise, 'ACEITA')
