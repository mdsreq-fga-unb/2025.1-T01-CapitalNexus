from datetime import timedelta
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.test import TestCase

from members.models import Advertencias, Cargo, Falta, HistoricoReserva, Justificativa, Material, Membro, MembroNucleo, Nucleo, Reuniao

class MembroModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testeuser', password='123456')

    def test_str_method(self):
        membro = Membro(user=self.user, matricula='123456789', nome='Fulano Teste', email='fulano@capitalrocketteam.com')
        self.assertEqual(str(membro), 'Fulano Teste, 123456789, fulano@capitalrocketteam.com')

    def test_email_validation_with_invalid_domain(self):
        membro = Membro(user=self.user, matricula='213456789', nome='Fulano Teste', email='fulano@gmail.com')
        with self.assertRaises(ValidationError):
            membro.clean()

    def test_email_validation_with_valid_domain(self):
        membro = Membro(user=self.user, matricula='133456789', nome='Fulano Teste', email='fulano@capitalrocketteam.com')
        try:
            membro.clean()  # Não deve lançar exceção
        except ValidationError:
            self.fail("clean() lançou ValidationError com domínio válido")

class MembroPermissaoTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='gestor', password='123456')
        self.nucleo_gestao = Nucleo.objects.create(nome='Gestão de Pessoas')
        self.membro = Membro.objects.create(user=self.user, matricula='999888777', nome='Gestor', email='gestor@capitalrocketteam.com')
        MembroNucleo.objects.create(membro=self.membro, nucleo=self.nucleo_gestao, cargo=Cargo.objects.create(posicao='Membro'))

    def test_is_gestor_true(self):
        self.assertTrue(self.membro.is_gestor())

    def test_is_gerente_false(self):
        self.assertFalse(self.membro.is_gerente())

class ReuniaoModelTest(TestCase):
    def test_str(self):
        reuniao = Reuniao.objects.create(
            titulo="Reunião de Teste",
            data_hora=timezone.now(),
            local="Sala 1",
            tipo="RG"
        )
        self.assertEqual(str(reuniao), "Reunião de Teste")

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
        # Cria núcleo e cargo apenas uma vez
        self.nucleo = Nucleo.objects.create(nome="Gestão de Pessoas")
        self.cargo = Cargo.objects.create(posicao="Gerente")

        # Usuário 1 - Gerente
        self.user_gerente = User.objects.create_user(username='gerente', password='123')
        self.membro_gerente = Membro.objects.create(
            user=self.user_gerente,
            matricula="000000001",
            nome="Gerente",
            email="gerente@capitalrocketteam.com"
        )
        MembroNucleo.objects.create(membro=self.membro_gerente, nucleo=self.nucleo, cargo=self.cargo)

        # Usuário 2 - Comum
        self.user_comum = User.objects.create_user(username='user1', password='123')
        self.membro_comum = Membro.objects.create(
            user=self.user_comum,
            matricula="000000002",
            nome="Usuário 1",
            email="user1@capitalrocketteam.com"
        )
        MembroNucleo.objects.create(membro=self.membro_comum, nucleo=self.nucleo, cargo=self.cargo)
        
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
        self.client.login(username='gerente', password='123')
        response = self.client.get(self.url_lista)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'members/justificativas.html')
        self.assertContains(response, self.justificativa.texto_justificativa) # Verifica se a justificativa pendente aparece

    def test_membro_comum_nao_pode_ver_pagina_de_avaliacao(self):
        """
        Testa se um membro comum é redirecionado ao tentar acessar a página de avaliação.

        Args:
            None

        Returns:
            None
        """
        print("Executando teste: test_membro_comum_nao_pode_ver_pagina_de_avaliacao")
        # NOTA: Este teste espera que a verificação 'is_gestor' na sua view esteja ativa (não comentada)
        self.client.login(username='membro', password='password')
        response = self.client.get(self.url_lista)
        
        # Esperamos um redirecionamento (código 302)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('membros:faltaseadvertencias')) # Verifica se redirecionou para o dashboard

    def test_gestor_pode_aprovar_justificativa(self):
        """
        Testa se um gestor pode aprovar uma justificativa com sucesso via POST.

        Args:
            None

        Returns:
            None
        """
        print("Executando teste: test_gestor_pode_aprovar_justificativa")
        self.client.login(username='gerente', password='123')
        
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

class GerenciarAdvertenciasTest(TestCase):
    """
    Conjunto de testes para as funcionalidades de listar, criar, editar
    e excluir advertências.
    """
    def setUp(self):
        """
        Prepara o ambiente inicial para os testes.

        Cria um usuário gestor, um membro comum, um núcleo e uma advertência
        para ser usada nos testes de edição e exclusão.

        Args:
            None

        Returns:
            None
        """
        # 1. Criar grupo, usuários e membros
        self.nucleo = Nucleo.objects.create(nome="Gestão de Pessoas")
        self.cargo = Cargo.objects.create(posicao="Gerente")
        self.user_gerente = User.objects.create_user(username='gerente', password='123')
        self.membro_gerente = Membro.objects.create(
            user=self.user_gerente,
            matricula="000000001",
            nome="Gerente",
            email="gerente@capitalrocketteam.com"
        )
        MembroNucleo.objects.create(membro=self.membro_gerente, nucleo=self.nucleo, cargo=self.cargo)

        self.membro_user = User.objects.create_user('membro_comum', 'membro@capitalrocketteam.com', 'password')
        self.membro_comum = Membro.objects.create(user=self.membro_user, matricula='191012345', nome='Membro Comum')

        # 2. Criar a advertência que será usada para testar edição e exclusão
        self.advertencia_existente = Advertencias.objects.create(
            membro=self.membro_comum,
            contexto="Contexto inicial para teste.",
        )

        # 3. URLs
        self.url_lista = reverse('membros:advertencias')
        self.url_nova = reverse('membros:criar-advertencia')
        self.url_editar = reverse('membros:editar-advertencia', kwargs={'advertencia_id': self.advertencia_existente.id})
        self.url_excluir = reverse('membros:excluir-advertencia', kwargs={'advertencia_id': self.advertencia_existente.id})

    def test_gestor_pode_acessar_pagina_de_advertencias(self):
        """
        Testa se um gestor logado consegue acessar a lista de advertências.

        Args:
            None

        Returns:
            None
        """
        self.client.login(username='gerente', password='123')
        response = self.client.get(self.url_lista)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'members/advertencias.html')
        self.assertContains(response, "Gerenciar Advertências") # Verifica se o conteúdo está na página

    def test_membro_comum_nao_pode_acessar_pagina_de_advertencias(self):
        """
        Testa se um membro comum é redirecionado ao tentar acessar a página.

        Args:
            None

        Returns:
            None
        """
        self.client.login(username='membro_comum', password='password')
        response = self.client.get(self.url_lista)
        self.assertEqual(response.status_code, 302) # Espera um redirecionamento
        self.assertRedirects(response, reverse('membros:faltaseadvertencias'))

    def test_gestor_pode_criar_nova_advertencia(self):
        """
        Testa se um gestor pode registrar uma nova advertência via POST.

        Args:
            None

        Returns:
            None
        """
        self.client.login(username='gerente', password='123')
        advertencias_antes = Advertencias.objects.count()
        
        form_data = {
            'membro': self.membro_comum.matricula, # O ModelChoiceField espera o ID (PK)
            'contexto': 'Nova advertência criada pelo teste.'
        }
        
        response = self.client.post(self.url_nova, data=form_data)

        self.assertEqual(Advertencias.objects.count(), advertencias_antes + 1)
        self.assertRedirects(response, self.url_lista)

    def test_gestor_pode_editar_advertencia(self):
        """
        Testa se um gestor pode atualizar o contexto de uma advertência.

        Args:
            None

        Returns:
            None
        """
        self.client.login(username='gerente', password='123')
        
        form_data = {
            'membro': self.membro_comum.matricula,
            'contexto': 'Contexto ATUALIZADO.'
        }
        
        response = self.client.post(self.url_editar, data=form_data)
        self.assertRedirects(response, self.url_lista)

        # Recarrega o objeto do banco de dados para pegar os dados atualizados
        self.advertencia_existente.refresh_from_db()
        
        # Verifica se o campo foi realmente alterado
        self.assertEqual(self.advertencia_existente.contexto, 'Contexto ATUALIZADO.')

    def test_gestor_pode_excluir_advertencia(self):
        """
        Testa se um gestor pode excluir uma advertência.

        Args:
            None

        Returns:
            None
        """
        self.client.login(username='gerente', password='123')
        advertencias_antes = Advertencias.objects.count()

        # A view de exclusão espera um POST para confirmar
        response = self.client.post(self.url_excluir)

        self.assertRedirects(response, self.url_lista)
        self.assertEqual(Advertencias.objects.count(), advertencias_antes - 1)

class MateriaisFuncionalidadeTest(TestCase):
    """
    Testa o ciclo de vida completo do gerenciamento de materiais:
    listar, filtrar, reservar e devolver.
    """
    def setUp(self):
        """
        Prepara o ambiente com um gestor, um membro comum, um núcleo,
        e dois materiais: um disponível e um em uso.
        """
        # --- Usuários e Permissões ---
        # gestao_group = Group.objects.create(name='Nucleo_Gestao')
        self.nucleo = Nucleo.objects.create(nome="Gerência")
        self.cargo = Cargo.objects.create(posicao="Gerente")
        self.user_gerente = User.objects.create_user(username='gestor', password='password123')
        self.membro_gerente = Membro.objects.create(
            user=self.user_gerente,
            matricula="000000001",
            nome="Gerente",
            email="gerente@capitalrocketteam.com"
        )
        MembroNucleo.objects.create(membro=self.membro_gerente, nucleo=self.nucleo, cargo=self.cargo)

        self.membro_user = User.objects.create_user('membro_mat', 'membro@capitalrocketteam.com', 'password')
        self.membro_comum = Membro.objects.create(user=self.membro_user, matricula='191012345', nome='Membro Comum')

        # --- Dados ---
        self.nucleo = Nucleo.objects.create(nome='Desenvolvimento', categoria='TECNICO')
        self.material_disponivel = Material.objects.create(
            nome='Notebook Dell',
            tipo='EQUIPAMENTO',
            finalidade='Desenvolvimento de software',
            quantidade_total=1,
            status='DISPONIVEL',
            nucleo_responsavel=self.nucleo
        )
        self.material_em_uso = Material.objects.create(
            nome='Tablet Wacom',
            tipo='EQUIPAMENTO',
            finalidade='Design',
            quantidade_total=1,
            status='EM_USO', # Este material já começa em uso
            nucleo_responsavel=self.nucleo
        )
        # Criamos o registro de histórico para o material que está em uso
        self.reserva_ativa = HistoricoReserva.objects.create(
            material=self.material_em_uso,
            membro=self.membro_comum,
            data_devolucao_prevista=timezone.now().date() + timedelta(days=5)
        )

        # --- URLs ---
        self.url_lista = reverse('membros:materiais')
        self.url_reservar = reverse('membros:reservar-material', kwargs={'material_id': self.material_disponivel.id})
        self.url_devolver = reverse('membros:devolver-material', kwargs={'material_id': self.material_em_uso.id})


    def test_lista_de_materiais_e_filtro(self):
        """
        Testa se a página de materiais carrega e se o filtro de status funciona.

        Args:
            None
        Returns:
            None
        """
        self.client.login(username='membro_mat', password='password')
        
        # Testa o acesso à página principal
        response = self.client.get(self.url_lista)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Notebook Dell') # Verifica se o material disponível aparece
        self.assertContains(response, 'Tablet Wacom')  # Verifica se o material em uso aparece

        # Testa o filtro para mostrar apenas materiais "EM_USO"
        response_filtrada = self.client.get(self.url_lista, {'status': 'EM_USO'})
        self.assertContains(response_filtrada, 'Tablet Wacom')
        self.assertNotContains(response_filtrada, 'Notebook Dell') # Garante que o disponível sumiu

    def test_membro_pode_reservar_material_disponivel(self):
        """
        Testa o fluxo completo de reservar um material.

        Args:
            None
        Returns:
            None
        """
        self.client.login(username='membro_mat', password='password')
        historico_antes = HistoricoReserva.objects.count()

        # Dados que seriam enviados pelo formulário da modal
        form_data = {
            'data_devolucao_prevista': timezone.now().date() + timedelta(days=10)
        }
        
        response = self.client.post(self.url_reservar, data=form_data)
        
        # Verifica o redirecionamento
        self.assertRedirects(response, self.url_lista)
        
        # Verifica se um novo registro de histórico foi criado
        self.assertEqual(HistoricoReserva.objects.count(), historico_antes + 1)

        # Recarrega o estado do material do banco de dados
        self.material_disponivel.refresh_from_db()
        # Verifica se o status do material mudou para 'EM_USO'
        self.assertEqual(self.material_disponivel.status, 'EM_USO')

    def test_membro_pode_devolver_material(self):
        """
        Testa o fluxo completo de devolução de um material.

        Args:
            None
        Returns:
            None
        """
        # Loga como o membro que está com o material
        self.client.login(username='membro_mat', password='password')

        # Enviamos um POST para a URL de devolução (não precisa de dados no form)
        response = self.client.post(self.url_devolver)
        
        self.assertRedirects(response, self.url_lista)

        # Recarrega os objetos do banco
        self.material_em_uso.refresh_from_db()
        self.reserva_ativa.refresh_from_db()

        # Verifica se o status do material voltou para 'DISPONIVEL'
        self.assertEqual(self.material_em_uso.status, 'DISPONIVEL')
        # Verifica se a data de devolução real foi preenchida no histórico
        self.assertIsNotNone(self.reserva_ativa.data_devolucao_real)