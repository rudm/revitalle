from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone

from cadastro import forms, models


def home(request):
    return render(request, 'home.html')


class AlunoList(ListView):
    model = models.Aluno
    template_name = 'cadastro/aluno/aluno_list.html'
    paginate_by = 10
    ordering = ['-ativo', 'nome']

    def get_queryset(self):
        queryset = super().get_queryset()

        search_term = self.request.GET.get('search')
        if search_term:
            # queryset = queryset.filter(Q(nome__unaccent__icontains=search_term))
            queryset = queryset.filter(Q(nome__icontains=search_term))

        order_by = self.request.GET.get('order_by')
        direction = self.request.GET.get('direction')

        if order_by and direction:
            return queryset.order_by(f'{"-" if direction == "desc" else ""}{order_by}')

        return queryset.order_by(*self.ordering)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_term'] = self.request.GET.get('search', '')
        context['current_order'] = self.request.GET.get('order_by', 'ativo')
        context['current_direction'] = self.request.GET.get('direction', 'desc')
        return context
    
    def render_to_response(self, context, **response_kwargs):
        if self.request.GET.get('ajax'):
            return render(self.request, 'cadastro/aluno/aluno_list_table.html', context)
        return super().render_to_response(context, **response_kwargs)


class AlunoDetail(DetailView):
    model = models.Aluno
    template_name = 'cadastro/aluno/aluno_detail.html'


class AlunoCreate(CreateView):
    model = models.Aluno
    form_class = forms.AlunoForm
    template_name = 'cadastro/aluno/aluno_form.html'
    success_url = reverse_lazy('cadastro:aluno-list')


class AlunoUpdate(UpdateView):
    model = models.Aluno
    form_class = forms.AlunoForm
    template_name = 'cadastro/aluno/aluno_form.html'
    success_url = reverse_lazy('cadastro:aluno-list')


class AlunoDelete(DeleteView):
    model = models.Aluno
    template_name = 'cadastro/aluno/aluno_delete.html'
    success_url = reverse_lazy('cadastro:aluno-list')


class ProfessorList(ListView):
    model = models.Professor
    template_name = 'cadastro/professor/professor_list.html'
    paginate_by = 10
    ordering = ['-ativo', 'nome']


class ProfessorDetail(DetailView):
    model = models.Professor
    template_name = 'cadastro/professor/professor_detail.html'


class ProfessorCreate(CreateView):
    model = models.Professor
    form_class = forms.ProfessorForm
    template_name = 'cadastro/professor/professor_form.html'
    success_url = reverse_lazy('cadastro:professor-list')


class ProfessorUpdate(UpdateView):
    model = models.Professor
    form_class = forms.ProfessorForm
    template_name = 'cadastro/professor/professor_form.html'
    success_url = reverse_lazy('cadastro:professor-list')


class ProfessorDelete(DeleteView):
    model = models.Professor
    template_name = 'cadastro/professor/professor_delete.html'
    success_url = reverse_lazy('cadastro:professor-list')


class FormaPgtoList(ListView):
    model = models.FormaPgto
    template_name = 'cadastro/formapgto/formapgto_list.html'
    paginate_by = 10
    ordering = ['descricao']


class FormaPgtoDetail(DetailView):
    model = models.FormaPgto
    template_name = 'cadastro/formapgto/formapgto_detail.html'


class FormaPgtoCreate(CreateView):
    model = models.FormaPgto
    form_class = forms.FormaPgtoForm
    template_name = 'cadastro/formapgto/formapgto_form.html'
    success_url = reverse_lazy('cadastro:formapgto-list')


class FormaPgtoUpdate(UpdateView):
    model = models.FormaPgto
    form_class = forms.FormaPgtoForm
    template_name = 'cadastro/formapgto/formapgto_form.html'
    success_url = reverse_lazy('cadastro:formapgto-list')


class FormaPgtoDelete(DeleteView):
    model = models.FormaPgto
    template_name = 'cadastro/formapgto/formapgto_delete.html'
    success_url = reverse_lazy('cadastro:formapgto-list')


class TipoDespesaList(ListView):
    model = models.TipoDespesa
    template_name = 'cadastro/tipodespesa/tipodespesa_list.html'
    paginate_by = 10
    ordering = ['descricao']


class TipoDespesaDetail(DetailView):
    model = models.TipoDespesa
    template_name = 'cadastro/tipodespesa/tipodespesa_detail.html'


class TipoDespesaCreate(CreateView):
    model = models.TipoDespesa
    form_class = forms.TipoDespesaForm
    template_name = 'cadastro/tipodespesa/tipodespesa_form.html'
    success_url = reverse_lazy('cadastro:tipodespesa-list')


class TipoDespesaUpdate(UpdateView):
    model = models.TipoDespesa
    form_class = forms.TipoDespesaForm
    template_name = 'cadastro/tipodespesa/tipodespesa_form.html'
    success_url = reverse_lazy('cadastro:tipodespesa-list')


class TipoDespesaDelete(DeleteView):
    model = models.TipoDespesa
    template_name = 'cadastro/tipodespesa/tipodespesa_delete.html'
    success_url = reverse_lazy('cadastro:tipodespesa-list')


class DespesaList(ListView):
    model = models.Despesa
    template_name = 'cadastro/despesa/despesa_list.html'
    paginate_by = 10
    ordering = ['dtlancamento']

    def get_queryset(self):
        mes = self.request.GET.get('mes_atual', timezone.now().month)
        ano = self.request.GET.get('ano_atual', timezone.now().year)
        queryset = models.Despesa.objects.select_related('tipodespesa').filter(
            dtlancamento__year=ano, dtlancamento__month=mes).order_by(*self.ordering)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anos'] = range(timezone.now().year + 1, 2000, -1)
        context['meses'] = range(1, 13)
        context['mes_atual'] = self.request.GET.get('mes', timezone.now().month)
        context['ano_atual'] = self.request.GET.get('ano', timezone.now().year)
        return context
    
    def render_to_response(self, context, **response_kwargs):
        if self.request.GET.get('ajax'):
            return render(self.request, 'cadastro/despesa/despesa_list_table.html', context)
        return super().render_to_response(context, **response_kwargs)


class DespesaDetail(DetailView):
    model = models.Despesa
    template_name = 'cadastro/despesa/despesa_detail.html'


class DespesaCreate(CreateView):
    model = models.Despesa
    form_class = forms.DespesaForm
    template_name = 'cadastro/despesa/despesa_form.html'
    success_url = reverse_lazy('cadastro:despesa-list')


class DespesaUpdate(UpdateView):
    model = models.Despesa
    form_class = forms.DespesaForm
    template_name = 'cadastro/despesa/despesa_form.html'
    success_url = reverse_lazy('cadastro:despesa-list')


class DespesaDelete(DeleteView):
    model = models.Despesa
    template_name = 'cadastro/despesa/despesa_delete.html'
    success_url = reverse_lazy('cadastro:despesa-list')


class ReceitaList(ListView):
    model = models.Receita
    queryset = models.Receita.objects.select_related('aluno', 'formapgto', 'professor')
    template_name = 'cadastro/receita/receita_list.html'
    paginate_by = 10
    ordering = ['dtlancamento']

    def get_queryset(self):
        mes = self.request.GET.get('mes_atual', timezone.now().month)
        ano = self.request.GET.get('ano_atual', timezone.now().year)
        queryset = models.Receita.objects.select_related('aluno', 'formapgto', 'professor').filter(
            dtlancamento__year=ano, dtlancamento__month=mes).order_by(*self.ordering)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anos'] = range(timezone.now().year + 1, 2000, -1)
        context['meses'] = range(1, 13)
        context['mes_atual'] = self.request.GET.get('mes', timezone.now().month)
        context['ano_atual'] = self.request.GET.get('ano', timezone.now().year)
        return context
    
    def render_to_response(self, context, **response_kwargs):
        if self.request.GET.get('ajax'):
            return render(self.request, 'cadastro/receita/receita_list_table.html', context)
        return super().render_to_response(context, **response_kwargs)


class ReceitaDetail(DetailView):
    model = models.Receita
    template_name = 'cadastro/receita/receita_detail.html'


class ReceitaCreate(CreateView):
    model = models.Receita
    form_class = forms.ReceitaForm
    template_name = 'cadastro/receita/receita_form.html'
    success_url = reverse_lazy('cadastro:receita-list')


class ReceitaUpdate(UpdateView):
    model = models.Receita
    form_class = forms.ReceitaForm
    template_name = 'cadastro/receita/receita_form.html'
    success_url = reverse_lazy('cadastro:receita-list')


class ReceitaDelete(DeleteView):
    model = models.Receita
    template_name = 'cadastro/receita/receita_delete.html'
    success_url = reverse_lazy('cadastro:receita-list')
