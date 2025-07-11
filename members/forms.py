# meu_app/forms.py
from django import forms
from django.utils import timezone
from .models import Reuniao
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