from django import forms
from django.forms.widgets import RadioSelect
from django.db.models import Max

from cadastro import models


class AlunoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        max_matricula = models.Aluno.objects.aggregate(Max('matricula'))['matricula__max']
        self.fields['matricula'].initial = max_matricula + 1

    class Meta:
        model = models.Aluno
        labels = {
            'dtnascimento': 'Data Nascimento',
            'matricula': 'Matrícula',
            'dtmatricula': 'Data Matrícula',
        }
        widgets = {
            'sexo': RadioSelect,
        }
        fields = (
            'matricula', 'nome', 'sexo', 'dtnascimento', 'dtmatricula', 'ativo',
        )


class ProfessorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        max_matricula = models.Professor.objects.aggregate(Max('matricula'))['matricula__max']
        self.fields['matricula'].initial = max_matricula + 1

    class Meta:
        model = models.Professor
        labels = {
            'dtnascimento': 'Data Nascimento',
            'matricula': 'Matrícula',
            'dtadmissao': 'Data Admissão',
        }
        widgets = {
            'sexo': RadioSelect,
        }
        fields = (
            'matricula', 'nome', 'sexo', 'dtnascimento', 'dtadmissao', 'ativo',
        )


class FormaPgtoForm(forms.ModelForm):

    class Meta:
        model = models.FormaPgto
        labels = {
            'descricao': 'Descrição',
            'tipo': 'Tipo',
        }
        fields = (
            'descricao', 'tipo',
        )


class TipoDespesaForm(forms.ModelForm):

    class Meta:
        model = models.TipoDespesa
        labels = {
            'descricao': 'Descrição',
        }
        fields = (
            'descricao',
        )


class DespesaForm(forms.ModelForm):

    class Meta:
        model = models.Despesa
        labels = {
            'dtlancamento': 'Data Lançamento',
            'tipodespesa': 'Tipo de Despesa',
            'observacao': 'Observação',
        }
        fields = (
            'dtlancamento', 'tipodespesa', 'valor', 'pago', 'observacao',
        )


class ReceitaForm(forms.ModelForm):

    class Meta:
        model = models.Receita
        labels = {
            'dtlancamento': 'Data Lançamento',
            'aluno': 'Aluno',
            'formapgto': 'Forma de Pagamento',
            'dtlancamento': 'Data Lançamento',
            'observacao': 'Observação',
        }
        fields = (
            'dtlancamento', 'aluno', 'formapgto', 'valor', 'professor', 'pago', 'observacao',
        )
