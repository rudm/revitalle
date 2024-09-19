from enum import IntEnum
from datetime import date

from django.db.models import (
    Model, AutoField, ForeignKey, DecimalField, IntegerField, SmallIntegerField, CharField,
    TextField, BooleanField, DateField, DateTimeField, PROTECT, CASCADE,
)


class Pessoa(Model):
    class Sexo(IntEnum):
        Masculino = 1
        Feminino = 2

    id = AutoField(primary_key=True)
    nome = CharField(max_length=60)
    matricula = IntegerField(unique=True)
    sexo = SmallIntegerField(
        choices=((s.value, s.name.title()) for s in Sexo), default=Sexo.Feminino)
    dtnascimento = DateField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        abstract = True


class Aluno(Pessoa):
    dtmatricula = DateField(default=date.today)
    ativo = BooleanField(default=True)

    class Meta:
        db_table = 'aluno'


class Professor(Pessoa):
    dtadmissao = DateField(default=date.today)

    class Meta:
        db_table = 'professor'


class FormaPgto(Model):
    class Tipo(IntEnum):
        Dinheiro = 1
        Cheque = 2
        Pix = 3
        Debito = 4
        Credito = 5

    descricao = CharField(max_length=60)
    tipo = SmallIntegerField(choices=((t.value, t.name.title()) for t in Tipo), default=1)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'formapgto'


class TipoDespesa(Model):
    descricao = CharField(max_length=60)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'tipodespesa'


class Despesa(Model):
    tipodespesa = ForeignKey(TipoDespesa, on_delete=PROTECT, null=True, blank=True)
    valor = DecimalField(max_digits=10, decimal_places=2)
    dtlancamento = DateField(default=date.today)
    pago = BooleanField(default=False)
    observacao = TextField(blank=True, null=True)

    class Meta:
        db_table = 'despesa'


class Receita(Model):
    aluno = ForeignKey(Aluno, on_delete=PROTECT)
    professor = ForeignKey(Professor, on_delete=PROTECT)
    formapgto = ForeignKey(FormaPgto, on_delete=PROTECT)
    valor = DecimalField(max_digits=10, decimal_places=2)
    dtlancamento = DateField(default=date.today)
    pago = BooleanField(default=False)
    observacao = TextField(blank=True, null=True)

    class Meta:
        db_table = 'receita'
