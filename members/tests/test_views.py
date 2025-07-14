from datetime import timedelta
from django.utils import timezone
import datetime
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from members.forms import ReuniaoForm
from members.models import Nucleo, MembroNucleo, Membro, Cargo, Reuniao

class MembroViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        self.user_gerente = User.objects.create_user(username='gerente', password='1234')
        self.user_nao_autorizado = User.objects.create_user(username='usuario', password='1234')

        self.nucleo = Nucleo.objects.create(nome='Gerência')
        self.cargo = Cargo.objects.create(posicao='Líder')

        self.membro_gerente = Membro.objects.create(user=self.user_gerente, matricula='202100001', nome='Gerente Nome', email='gerente@capitalrocketteam.com')
        MembroNucleo.objects.create(membro=self.membro_gerente, nucleo=self.nucleo, cargo=self.cargo)

        self.membro_nao_autorizado = Membro.objects.create(user=self.user_nao_autorizado, matricula='202100002', nome='Comum Nome', email='usuario@capitalrocketteam.com')

    # def test_pagina_lista_membros_requer_login(self):
    #     response = self.client.get(reverse('membros:membros'))
    #     self.assertRedirects(response, '/accounts/login/?next=' + reverse('membros:membros'))

    def test_membro_novo_somente_gerente(self):
        self.client.login(username='usuario', password='1234')
        response = self.client.post(reverse('membros:membro-novo'), {})
        self.assertRedirects(response, reverse('membros:membros'))

        self.client.login(username='gerente', password='1234')
        post_data = {
            'username': 'novo',
            'first_name': 'Novo',
            'last_name': 'Membro',
            'email': 'novo@capitalrocketteam.com',
            'password': 'senha123',
            'matricula': '202100003',
            'nucleo': self.nucleo.pk,
            'cargo': self.cargo.pk,
        }
        response = self.client.post(reverse('membros:membro-novo'), data=post_data)
        self.assertRedirects(response, reverse('membros:membros'))
        self.assertTrue(User.objects.filter(username='novo').exists())

    def test_membro_editar_permissoes(self):
        self.client.login(username='usuario', password='1234')
        response = self.client.get(reverse('membros:editar-membro', args=['202100001']))
        self.assertRedirects(response, reverse('membros:membros'))

        self.client.login(username='gerente', password='1234')
        response = self.client.get(reverse('membros:editar-membro', args=['202100001']))
        self.assertEqual(response.status_code, 200)

    def test_membro_excluir_somente_gerente(self):
        self.client.login(username='usuario', password='1234')
        response = self.client.post(reverse('membros:excluir-membro', args=['202100001']))
        self.assertRedirects(response, reverse('membros:membros'))

class ViewReunioesTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='gerente', password='123')
        self.membro = Membro.objects.create(user=self.user, matricula="000000001", nome="Teste", email="teste@capitalrocketteam.com")
        self.membro.membronucleo_set.create(nucleo_id=1, cargo_id=1)  # Adapte para seus IDs de teste
        self.nucleo = Nucleo.objects.create(nome="Gestão de Pessoas")
        self.cargo = Cargo.objects.create(posicao='Gerente')

        self.user = User.objects.create_user(username="user1", password="123")
        self.membro = Membro.objects.create(
            user=self.user,
            matricula="000000002",
            nome="Usuário 1",
            email="user1@capitalrocketteam.com"
        )
        MembroNucleo.objects.create(membro=self.membro, nucleo=self.nucleo, cargo=self.cargo)


    def test_acesso_lista_reunioes(self):
        self.client.login(username='gerente', password='123')
        response = self.client.get(reverse('membros:reunioes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'members/reunioes.html')

class ReuniaoFormTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='gerente', password='123')
        self.nucleo = Nucleo.objects.create(nome='Gestão de Pessoas')  # ou outro nome válido
        self.cargo = Cargo.objects.create(posicao='Gerente')
        self.membro = Membro.objects.create(
            user=self.user, 
            matricula="000000004", 
            nome="Teste", 
            email="teste@capitalrocketteam.com"
        )

        MembroNucleo.objects.create(membro=self.membro, nucleo=self.nucleo, cargo=self.cargo)


    def test_data_hora_combinada_valida(self):
        data = timezone.now().date() + datetime.timedelta(days=1)
        hora = datetime.time(10, 0)
        form_data = {
            'titulo': 'Reunião de Teste',
            'local': 'Sala A',
            'tipo': 'RG',
            'data': data,
            'hora': hora
        }
        form = ReuniaoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_data_hora_passada(self):
        data = timezone.now().date() - datetime.timedelta(days=1)
        hora = datetime.time(10, 0)
        form_data = {
            'titulo': 'Reunião de Ontem',
            'local': 'Sala A',
            'tipo': 'RG',
            'data': data,
            'hora': hora
        }
        form = ReuniaoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('data', form.errors)
