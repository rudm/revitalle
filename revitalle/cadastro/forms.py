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
            'sttipo': 'Tipo',
        }
        fields = (
            'descricao', 'sttipo',
        )


class PagamentoForm(forms.ModelForm):

    class Meta:
        model = models.Pagamento
        labels = {
            'formapgto': 'Forma de Pagamento',
            'dtpagamento': 'Data Pagamento',
            'observacao': 'Observação',
        }
        fields = (
            'aluno', 'formapgto', 'valor', 'dtpagamento', 'observacao',
        )
