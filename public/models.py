from django.db import models

# Create your models here.

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