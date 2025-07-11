from django.db import models
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError

class Membro(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    matricula = models.CharField(max_length=9, primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def clean(self):
        super().clean()
        dominio = "@capitalrocketteam.com"
        if not self.email.endswith(dominio):
            raise ValidationError({'email': f"O e-mail deve ter o domínio '{dominio}'."})

    def is_gestor(self):
        # Verifica se este membro está associado ao 'Núcleo de Gestão' através do modelo MembroNucleo.
        return self.membronucleo_set.filter(nucleo__nome='Gestão de Pessoas').exists()

    def is_gerente(self):
        # Verifica se este membro está associado ao núcleo de gerência
        return self.membronucleo_set.filter(nucleo__nome='Gerência').exists()

    def is_marketeiro(self):
        # Verifica se este membro está associado ao núcleo de marketing
        return self.membronucleo_set.filter(nucleo__nome='Marketing').exists()

    def __str__(self):
        return f"{self.nome}, {self.matricula}, {self.email}"
    
class Nucleo(models.Model):
    nome = models.CharField(max_length=64)
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
    
class Reuniao(models.Model):
    TIPO_CHOICES = [
        ('RG', 'Reunião Geral'),
        ('PC', 'Ponto de controle'),
    ]
    titulo = models.CharField(max_length=200)
    data_hora = models.DateTimeField()
    local = models.CharField(max_length=100)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES, default='PC')
    ata = models.FileField(upload_to='atas/', blank=True, null=True)

    class Meta:
        ordering = ['data_hora']

    def __str__(self):
        return self.titulo
    
class Falta(models.Model):
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE)
    reuniao = models.ForeignKey(Reuniao, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('membro', 'reuniao')

    def __str__(self):
        return f"Falta em {self.reuniao.titulo}"
    
class Justificativa(models.Model):
    STATUS_ANALISE = [
        ('PENDENTE', 'Pendente'),
        ('ACEITA', 'Aceita'),
        ('REJEITADA', 'Rejeitada'),
    ]

    falta = models.OneToOneField(Falta, on_delete=models.CASCADE)
    texto_justificativa = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    status_analise = models.CharField(max_length=20, choices=STATUS_ANALISE, default='PENDENTE')
    feedback_analise = models.TextField(blank=True, null=True, help_text="Feedback do Núcleo X sobre a análise.")

    def __str__(self):
        return f"Justificativa de {self.falta.membro.nome} para falta em {self.falta.reuniao.titulo}."

class Advertencias(models.Model):
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE)
    contexto = models.CharField(max_length = 100)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('membro', 'id')
    
    def __str__(self):
        return f"Advertência do {self.membro.nome} por {self.contexto}."
