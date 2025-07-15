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
    
    def is_admfin(self):
        # Verifica se este membro está associado ao núcleo de administrativo financeiro
        return self.membronucleo_set.filter(nucleo__nome='Administrativo Financeiro').exists()

    def __str__(self):
        return f"{self.nome}, {self.matricula}, {self.email}"
    
class Nucleo(models.Model):
    # 1. Definimos as opções como uma lista de tuplas
    CATEGORIA_CHOICES = [
        ('TECNICO', 'Técnico'),
        ('GESTAO', 'Gestão'),
    ]

    nome = models.CharField(max_length=64)
    # 2. Adicionamos o argumento 'choices' ao nosso campo
    categoria = models.CharField(max_length=8, choices=CATEGORIA_CHOICES)

    class Meta:
        verbose_name='Núcleo'
        verbose_name_plural='Núcleos'
        
    def __str__(self):
        return self.nome
    
# class Nucleo(models.Model):
#     nome = models.CharField(max_length=64)
#     categoria = models.CharField(max_length=8)

#     class Meta:
#         verbose_name='Núcleo'
#         verbose_name_plural='Núcleos'
#     def __str__(self):
#         return self.nome
    
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
    
class Material(models.Model):
    TIPO_CHOICES = [
        ('EQUIPAMENTO', 'Equipamento'),
        ('CONSUMIVEL', 'Consumível'),
        ('ELETRONICO', 'Eletrônico'),
        ('OUTRO', 'Outro'),
    ]
    STATUS_CHOICES = [
        ('DISPONIVEL', 'Disponível'),
        ('EM_USO', 'Em uso'),
        ('MANUTENCAO', 'Em manutenção'),
    ]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    finalidade = models.CharField(max_length=200)
    quantidade_total = models.PositiveIntegerField(default=1)
    
    # Rastreia o status 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DISPONIVEL')  

    # O núcleo responsável pelo material
    nucleo_responsavel = models.ForeignKey(Nucleo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome
    
    def get_reserva_ativa(self):
        """
        Busca no histórico a última reserva para este material que ainda
        não foi devolvida (ou seja, a reserva ativa).
        """
        # Acessa o histórico através do related_name="historico" que definimos
        reserva = self.historico.filter(data_devolucao_real__isnull=True).first()
        return reserva
    
class HistoricoReserva(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="historico")
    membro = models.ForeignKey(Membro, on_delete=models.SET_NULL, null=True, help_text="Membro que retirou o material")
    data_retirada = models.DateTimeField(auto_now_add=True)
    data_devolucao_prevista = models.DateField()
    data_devolucao_real = models.DateTimeField(null=True, blank=True, help_text="Preenchido quando o material é devolvido")

    class Meta:
        ordering = ['-data_retirada']

    def __str__(self):
        return f"{self.material.nome} retirado por {self.membro.nome}"

# meu_app/models.py

class SolicitacaoMaterial(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('APROVADA', 'Aprovada'),
        ('REJEITADA', 'Rejeitada'),
        ('COMPRADO', 'Comprado'),
    ]

    solicitante = models.ForeignKey(Membro, on_delete=models.CASCADE)
    nome_material = models.CharField(max_length=150)
    justificativa = models.TextField(help_text="Explique por que este material é necessário.")
    quantidade = models.PositiveIntegerField(default=1)
    link_referencia = models.URLField(max_length=500, blank=True, null=True, help_text="Link de onde comprar o produto (opcional)")
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    feedback_gestao = models.TextField(blank=True, null=True, help_text="Feedback do gestor ao analisar o pedido.")

    class Meta:
        ordering = ['-data_solicitacao']

    def __str__(self):
        return f"Pedido de '{self.nome_material}' por {self.solicitante.nome}"

