from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cadastro import forms, models


def home(request):
    return render(request, 'home.html')


class AlunoList(ListView):
    model = models.Aluno
    template_name = 'cadastro/aluno/aluno_list.html'
    paginate_by = 10
    ordering = ['nome']

    def get_queryset(self):
        queryset = super().get_queryset()
        order_by = self.request.GET.get('order_by', 'matricula')
        direction = self.request.GET.get('direction', 'asc')
        return queryset.order_by(f'{"-" if direction == "desc" else ""}{order_by}')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_order'] = self.request.GET.get('order_by', 'matricula')
        context['current_direction'] = self.request.GET.get('direction', 'asc')
        return context


class AlunoDetail(DetailView):
    model = models.Aluno
    template_name = 'cadastro/aluno/aluno_detail.html'


class AlunoCreate(CreateView):
    model = models.Aluno
    form_class = forms.AlunoForm
    template_name = 'cadastro/aluno/aluno_form.html'
    success_url = reverse_lazy('cadastro:alunos')


class AlunoUpdate(UpdateView):
    model = models.Aluno
    form_class = forms.AlunoForm
    template_name = 'cadastro/aluno/aluno_form.html'
    success_url = reverse_lazy('cadastro:alunos')


class AlunoDelete(DeleteView):
    model = models.Aluno
    template_name = 'cadastro/aluno/aluno_delete.html'
    success_url = reverse_lazy('cadastro:alunos')


class ProfessorList(ListView):
    model = models.Professor
    template_name = 'cadastro/professor/professor_list.html'
    paginate_by = 10
    ordering = ['nome']


class ProfessorDetail(DetailView):
    model = models.Professor
    template_name = 'cadastro/professor/professor_detail.html'


class ProfessorCreate(CreateView):
    model = models.Professor
    form_class = forms.ProfessorForm
    template_name = 'cadastro/professor/professor_form.html'
    success_url = reverse_lazy('cadastro:professores')


class ProfessorUpdate(UpdateView):
    model = models.Professor
    form_class = forms.ProfessorForm
    template_name = 'cadastro/professor/professor_form.html'
    success_url = reverse_lazy('cadastro:professores')


class ProfessorDelete(DeleteView):
    model = models.Professor
    template_name = 'cadastro/professor/professor_delete.html'
    success_url = reverse_lazy('cadastro:professores')


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
    success_url = reverse_lazy('cadastro:formaspgto')


class FormaPgtoUpdate(UpdateView):
    model = models.FormaPgto
    form_class = forms.FormaPgtoForm
    template_name = 'cadastro/formapgto/formapgto_form.html'
    success_url = reverse_lazy('cadastro:formaspgto')


class FormaPgtoDelete(DeleteView):
    model = models.FormaPgto
    template_name = 'cadastro/formapgto/formapgto_delete.html'
    success_url = reverse_lazy('cadastro:formaspgto')


class PagamentoList(ListView):
    model = models.Pagamento
    queryset = models.Pagamento.objects.select_related('aluno', 'formapgto')
    template_name = 'cadastro/pagamento/pagamento_list.html'


class PagamentoDetail(DetailView):
    model = models.Pagamento
    template_name = 'cadastro/pagamento/pagamento_detail.html'


class PagamentoCreate(CreateView):
    model = models.Pagamento
    form_class = forms.PagamentoForm
    template_name = 'cadastro/pagamento/pagamento_form.html'
    success_url = reverse_lazy('cadastro:pagamentos')


class PagamentoUpdate(UpdateView):
    model = models.Pagamento
    form_class = forms.PagamentoForm
    template_name = 'cadastro/pagamento/pagamento_form.html'
    success_url = reverse_lazy('cadastro:pagamentos')


class PagamentoDelete(DeleteView):
    model = models.Pagamento
    template_name = 'cadastro/pagamento/pagamento_delete.html'
    success_url = reverse_lazy('cadastro:pagamentos')
