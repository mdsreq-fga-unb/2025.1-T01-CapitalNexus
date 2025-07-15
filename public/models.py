from django.db import models

# Create your models here.

class Patrocinador(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='project_images/')
    
    class Meta:
        verbose_name='Patrocinador'
        verbose_name_plural='Patrocinadores'
    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    resumo = models.TextField(help_text="Projeto desenvolvido de x - x, para participar ... e validar x.")
    imagem = models.ImageField(upload_to='project_images/')
    dimensoes = models.TextField(help_text="Foguete para 1km de apogeu, com 2.13m de comprimento, 15.5cm de diâmetro e 28kg.")
    situacao = models.TextField(help_text="Lançado em 2022 na LASC, conseguindo o 1° lugar em 2022.")
    custo = models.TextField(help_text="O custo foi de R$XX.XXX,XX")

    def __str__(self):
        return self.titulo
    def ano_display(self):
        if self.ano_fim:
            return f"{self.ano_inicio} - {self.ano_fim}"
        return f"{self.ano_inicio} - Atualmente"

class MensagemContato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    lido = models.BooleanField(default=False)

    class Meta:
        # Ordena as mensagens da mais nova para a mais antiga
        ordering = ['-data_envio']
        # Nome que aparecerá no painel de admin
        verbose_name = 'Mensagem de Contato'
        verbose_name_plural = 'Mensagens de Contato'

    def __str__(self):
        return f"Mensagem de {self.nome} em {self.data_envio.strftime('%d/%m/%Y %H:%M')}"
    
class ApresentacaoEquipe(models.Model):
    titulo = models.CharField(max_length=100, default="A Equipe")
    descricao = models.TextField()
    foto_equipe = models.ImageField(upload_to='fotos_equipe/')
    
    # Garante que só haverá uma entrada para esta seção
    def save(self, *args, **kwargs):
        self.pk = 1
        super(ApresentacaoEquipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

class Topico(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return self.titulo