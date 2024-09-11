from django.urls import path

from . import views

app_name = 'cadastro'

urlpatterns = [
    path('', views.home, name='home'),

    path('aluno', views.AlunoList.as_view(), name='alunos'),
    path('aluno/<int:pk>/', views.AlunoDetail.as_view(), name='aluno'),
    path('aluno-create/', views.AlunoCreate.as_view(), name='aluno-create'),
    path('aluno-update/<int:pk>/', views.AlunoUpdate.as_view(), name='aluno-update'),
    path('aluno-delete/<int:pk>/', views.AlunoDelete.as_view(), name='aluno-delete'),

    path('professor', views.ProfessorList.as_view(), name='professores'),
    path('professor/<int:pk>/', views.ProfessorDetail.as_view(), name='professor'),
    path('professor-create/', views.ProfessorCreate.as_view(), name='professor-create'),
    path('professor-update/<int:pk>/', views.ProfessorUpdate.as_view(), name='professor-update'),
    path('professor-delete/<int:pk>/', views.ProfessorDelete.as_view(), name='professor-delete'),

    path('formapgto', views.FormaPgtoList.as_view(), name='formaspgto'),
    path('formapgto/<int:pk>/', views.FormaPgtoDetail.as_view(), name='formapgto'),
    path('formapgto-create/', views.FormaPgtoCreate.as_view(), name='formapgto-create'),
    path('formapgto-update/<int:pk>/', views.FormaPgtoUpdate.as_view(), name='formapgto-update'),
    path('formapgto-delete/<int:pk>/', views.FormaPgtoDelete.as_view(), name='formapgto-delete'),

    path('pagamento', views.PagamentoList.as_view(), name='pagamentos'),
    path('pagamento/<int:pk>/', views.PagamentoDetail.as_view(), name='pagamento'),
    path('pagamento-create/', views.PagamentoCreate.as_view(), name='pagamento-create'),
    path('pagamento-update/<int:pk>/', views.PagamentoUpdate.as_view(), name='pagamento-update'),
    path('pagamento-delete/<int:pk>/', views.PagamentoDelete.as_view(), name='pagamento-delete'),
]
