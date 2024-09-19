from django import forms

from cadastro import models


class AlunoForm(forms.ModelForm):

    class Meta:
        model = models.Aluno
        labels = {
            'dtnascimento': 'Data Nascimento',
            'matricula': 'Matrícula',
            'dtmatricula': 'Data Matrícula',
        }
        fields = (
            'matricula', 'nome', 'sexo', 'dtnascimento', 'dtmatricula', 'ativo',
        )


class ProfessorForm(forms.ModelForm):

    class Meta:
        model = models.Professor
        labels = {
            'dtnascimento': 'Data Nascimento',
            'matricula': 'Matrícula',
            'dtadmissao': 'Data Admissão',
        }
        fields = (
            'matricula', 'nome', 'sexo', 'dtnascimento', 'dtadmissao',
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
