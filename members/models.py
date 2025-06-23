from django.db import models

class Membro(models.Model): 
    matricula = models.CharField(max_length=9, primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nome}, {self.matricula}, {self.email}"
    
class Nucleo(models.Model):
    nome = models.CharField(max_length=64, primary_key=True)
    categoria = models.CharField(max_length=8)

    class Meta:
        verbose_name='Núcleo'
        verbose_name_plural='Núcleos'
    def __str__(self):
        return self.nome
    
class Cargo(models.Model):
    posicao = models.CharField(max_length=64)

    def __str__(self):
        return self.posicao
    
class MembroNucleo(models.Model):
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE)
    nucleo = models.ForeignKey(Nucleo, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('membro', 'nucleo')
        verbose_name='Associação'
        verbose_name_plural='Associações'

    def __str__(self):
        return f"{self.membro.nome}, do núcleo {self.nucleo.nome} com o cargo de {self.cargo.posicao}"