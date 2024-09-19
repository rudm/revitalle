from django.urls import path

from . import views

app_name = 'cadastro'

urlpatterns = [
    path('', views.home, name='home'),

    path('aluno', views.AlunoList.as_view(), name='aluno-list'),
    path('aluno/<int:pk>/', views.AlunoDetail.as_view(), name='aluno-detail'),
    path('aluno-create/', views.AlunoCreate.as_view(), name='aluno-create'),
    path('aluno-update/<int:pk>/', views.AlunoUpdate.as_view(), name='aluno-update'),
    path('aluno-delete/<int:pk>/', views.AlunoDelete.as_view(), name='aluno-delete'),

    path('professor', views.ProfessorList.as_view(), name='professor-list'),
    path('professor/<int:pk>/', views.ProfessorDetail.as_view(), name='professor-detail'),
    path('professor-create/', views.ProfessorCreate.as_view(), name='professor-create'),
    path('professor-update/<int:pk>/', views.ProfessorUpdate.as_view(), name='professor-update'),
    path('professor-delete/<int:pk>/', views.ProfessorDelete.as_view(), name='professor-delete'),

    path('formapgto', views.FormaPgtoList.as_view(), name='formapgto-list'),
    path('formapgto/<int:pk>/', views.FormaPgtoDetail.as_view(), name='formapgto-detail'),
    path('formapgto-create/', views.FormaPgtoCreate.as_view(), name='formapgto-create'),
    path('formapgto-update/<int:pk>/', views.FormaPgtoUpdate.as_view(), name='formapgto-update'),
    path('formapgto-delete/<int:pk>/', views.FormaPgtoDelete.as_view(), name='formapgto-delete'),

    path('tipodespesa', views.TipoDespesaList.as_view(), name='tipodespesa-list'),
    path('tipodespesa/<int:pk>/', views.TipoDespesaDetail.as_view(), name='tipodespesa-detail'),
    path('tipodespesa-create/', views.TipoDespesaCreate.as_view(), name='tipodespesa-create'),
    path('tipodespesa-update/<int:pk>/', views.TipoDespesaUpdate.as_view(), name='tipodespesa-update'),
    path('tipodespesa-delete/<int:pk>/', views.TipoDespesaDelete.as_view(), name='tipodespesa-delete'),

    path('despesa', views.DespesaList.as_view(), name='despesa-list'),
    path('despesa/<int:pk>/', views.DespesaDetail.as_view(), name='despesa-detail'),
    path('despesa-create/', views.DespesaCreate.as_view(), name='despesa-create'),
    path('despesa-update/<int:pk>/', views.DespesaUpdate.as_view(), name='despesa-update'),
    path('despesa-delete/<int:pk>/', views.DespesaDelete.as_view(), name='despesa-delete'),

    path('receita', views.ReceitaList.as_view(), name='receita-list'),
    path('receita/<int:pk>/', views.ReceitaDetail.as_view(), name='receita-detail'),
    path('receita-create/', views.ReceitaCreate.as_view(), name='receita-create'),
    path('receita-update/<int:pk>/', views.ReceitaUpdate.as_view(), name='receita-update'),
    path('receita-delete/<int:pk>/', views.ReceitaDelete.as_view(), name='receita-delete'),
]
