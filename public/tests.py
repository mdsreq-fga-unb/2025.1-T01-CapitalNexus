# meu_app/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import MensagemContato

class ContatoViewTest(TestCase):

    def setUp(self):
        """Prepara o ambiente, pegando a URL da página de contato."""
        print("Executando setUp para ContatoViewTest")
        # Use o 'name' da sua URL de contato em urls.py
        self.contato_url = reverse('publico:contato')

    def test_formulario_contato_envio_sucesso(self):
        """
        Testa se um formulário de contato válido é salvo, redireciona para a mesma página
        e exibe uma mensagem de sucesso.
        """
        print("Executando teste: test_formulario_contato_envio_sucesso")

        mensagens_antes = MensagemContato.objects.count()

        form_data = {
            'nome': 'Visitante Teste',
            'email': 'visitante@gmail.com',
            'mensagem': 'Esta é uma mensagem de teste.',
            'termos': 'on'
        }
        # Isso diz ao cliente de teste para seguir o redirecionamento após o POST.
        response = self.client.post(self.contato_url, data=form_data, follow=True)

        # 1. Afirmamos que a PÁGINA FINAL (após o redirect) carregou com sucesso (código 200)
        self.assertEqual(response.status_code, 200)

        # 2. Afirmamos que, no final do processo, a URL que estamos vendo é a da própria página de contato.
        # Usamos response.request['PATH_INFO'] para pegar a URL da página final.
        self.assertEqual(response.request['PATH_INFO'], self.contato_url)

        # 3. Verificamos se a mensagem de sucesso está presente no HTML da página final.
        self.assertContains(response, "Sua mensagem foi enviada com sucesso!")

        # 4. Afirmamos que a mensagem foi salva no banco de dados.
        self.assertEqual(MensagemContato.objects.count(), mensagens_antes + 1)
