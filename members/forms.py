# meu_app/forms.py
from django import forms
from django.utils import timezone
from .models import Advertencias, HistoricoReserva, Justificativa, Reuniao, Material, SolicitacaoMaterial
import datetime

class FaltaForm(forms.Form):
    membro_matricula = forms.CharField(widget=forms.HiddenInput())
    # O checkbox em si. required=False é importante, pois não marcar é uma ação válida (presente).
    faltou = forms.BooleanField(required=False)

class ReuniaoForm(forms.ModelForm):
    # 1. Criamos os campos separados que o usuário vai ver
    data = forms.DateField(
        label="Data da Reunião",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    hora = forms.TimeField(
        label="Hora da Reunião",
        widget=forms.TimeInput(attrs={'type': 'time'})
    )

    class Meta:
        model = Reuniao
        # 2. Incluímos todos os campos do modelo, EXCETO o 'data_hora' original,
        #    pois vamos construí-lo a partir dos nossos campos 'data' e 'hora'.
        fields = ['titulo', 'local', 'tipo', 'ata']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ex: Reunião de Planejamento'}),
            'local': forms.TextInput(attrs={'placeholder': 'Ex: Auditório do UAC'}),
            'ata': forms.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        """
        Este método é executado sempre que o formulário é criado.
        """
        super().__init__(*args, **kwargs)
        # Adiciona o atributo 'min' ao campo de data para validação no front-end
        self.fields['data'].widget.attrs['min'] = timezone.now().strftime('%Y-%m-%d')
        
        # Verificamos se o formulário foi iniciado com uma instância 
        if self.instance and self.instance.pk:
            # Se a instância tem uma data e hora já salvas...
            if self.instance.data_hora:
                # ...nós separamos os valores...
                data_salva = self.instance.data_hora.date()
                hora_salva = self.instance.data_hora.time()
                
                # ...e os colocamos como valores iniciais para os nossos campos de formulário.
                self.initial['data'] = data_salva
                self.initial['hora'] = hora_salva

    def clean(self):
        # 3. Este método é executado durante a validação para "limpar" e combinar os dados
        cleaned_data = super().clean()
        data_form = cleaned_data.get("data")
        hora_form = cleaned_data.get("hora")

        if data_form and hora_form:
            # Combina a data e a hora em um único objeto datetime
            data_hora_combinada = datetime.datetime.combine(data_form, hora_form)
            # Adiciona o timezone local para evitar avisos
            data_hora_combinada = timezone.make_aware(data_hora_combinada)

            # Validação para garantir que a data/hora combinada não está no passado
            if data_hora_combinada < timezone.now():
                # Adiciona um erro ao campo 'data', que será exibido no formulário
                self.add_error('data', "A data e hora da reunião não podem ser no passado.")
            
            # Adiciona o valor combinado ao dicionário de dados limpos
            cleaned_data['data_hora'] = data_hora_combinada
            
        return cleaned_data

    def save(self, commit=True):
        # 4. Sobrescrevemos o método save para usar nosso campo combinado
        instance = super().save(commit=False)
        instance.data_hora = self.cleaned_data['data_hora']
        if commit:
            instance.save()
        return instance

class JustificativaForm(forms.ModelForm):
    class Meta:
        model = Justificativa
        # O usuário só precisa preencher a descrição. Os outros campos são automáticos.
        fields = ['texto_justificativa']
        widgets = {
            'texto_justificativa': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Descreva o motivo da sua ausência...'})
        }
        labels = {
            'texto_justificativa': 'Sua Justificativa'
        }

class AdvertenciaForm(forms.ModelForm):
    class Meta:
        model = Advertencias
        fields = ['membro', 'contexto']
        labels = {
            'membro': 'Selecione um membro',
            'contexto': 'Motivo / Contexto da Advertência'
        }
        widgets = {
            'membro': forms.Select(attrs={'id': 'select-membro-advertencia'}),
            'contexto': forms.Textarea(attrs={'rows': 4})
        }

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        # Definimos os campos que o usuário pode preencher
        fields = ['nome', 'tipo', 'finalidade', 'quantidade_total', 'nucleo_responsavel', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # # Deixa o campo 'em_uso_por' opcional, já que só é usado quando o status é 'EM_USO'
        # self.fields['em_uso_por'].required = False

class ReservaForm(forms.ModelForm):
    class Meta:
        model = HistoricoReserva
        fields = ['data_devolucao_prevista']
        widgets = {
            'data_devolucao_prevista': forms.DateInput(attrs={'type': 'date'})
        }
        labels = {
            'data_devolucao_prevista': 'Data Prevista de Devolução'
        }

    def __init__(self, *args, **kwargs):
        """
        Este método é executado sempre que o formulário é criado.
        Vamos usá-lo para adicionar a validação de front-end.
        """
        super().__init__(*args, **kwargs)
        
        # 1. Validação no Front-end: Define a data mínima no input HTML
        hoje_formatado = timezone.now().strftime('%Y-%m-%d')
        self.fields['data_devolucao_prevista'].widget.attrs['min'] = hoje_formatado


    def clean_data_devolucao_prevista(self):
        """
        Esta é uma função de validação customizada para o campo 'data_devolucao_prevista'.
        O Django a executa automaticamente durante a validação do formulário no back-end.
        """
        # 2. Validação no Back-end: Garante que a data não está no passado
        data_selecionada = self.cleaned_data.get('data_devolucao_prevista')
        hoje = timezone.now().date() # Pegamos apenas a data de hoje, sem a hora

        # Garante que o campo foi preenchido antes de comparar
        if data_selecionada and data_selecionada < hoje:
            # Se a data selecionada for anterior a hoje, lança um erro de validação.
            raise forms.ValidationError("A data de devolução não pode ser um dia no passado.")
        
        # Sempre retorne o dado "limpo" no final da função de validação
        return data_selecionada
    
class SolicitacaoMaterialForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoMaterial
        # O usuário só precisa preencher estes campos. O resto é automático.
        fields = ['nome_material', 'quantidade', 'justificativa', 'link_referencia']
        labels = {
            'nome_material': 'Nome do Material ou Equipamento',
            'quantidade': 'Quantidade Necessária',
            'justificativa': 'Finalidade de Uso / Justificativa',
            'link_referencia': 'Link de Referência (opcional)',
        }
