from django.test import TestCase
from django.contrib.auth.models import User 
from django.urls import reverse 
from members.models import Membro

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