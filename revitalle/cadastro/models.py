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
    matricula = CharField(unique=True)
    sexo = SmallIntegerField(
        choices=((s.value, s.name.title()) for s in Sexo), default=Sexo.Feminino)
    dtnascimento = DateField()

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
    class StTipo(IntEnum):
        Dinheiro = 1
        Cheque = 2
        Pix = 3
        Debito = 4
        Credito = 5

    descricao = CharField(max_length=60)
    sttipo = SmallIntegerField(choices=((m.value, m.name.title()) for m in StTipo), default=0)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'formapgto'


class Pagamento(Model):
    aluno = ForeignKey(Aluno, on_delete=PROTECT)
    formapgto = ForeignKey(FormaPgto, on_delete=PROTECT)
    valor = DecimalField(max_digits=10, decimal_places=2)
    dtpagamento = DateField(default=date.now)
    observacao = TextField(blank=True, null=True)

    class Meta:
        db_table = 'pagamento'
