from django.urls import path
from hogwarts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.register, name='signup'),
    path('area_logada/', views.area_logada, name='area_logada'),
    path('alunos/', views.AlunoListView.as_view(), name='aluno_list'),
    path('aluno/<uuid:pk>', views.AlunoDetailView.as_view(), name='aluno_detail'),  
    path('aluno/create/', views.CreateAluno.as_view(), name='aluno_create'),
    path('aluno/update/<uuid:pk>', views.UpdateAluno.as_view(), name='aluno_update'),
    path('aluno/delete/<uuid:pk>', views.DeleteAluno.as_view(), name='aluno_delete'),
    path('casa/<int:pk>', views.CasaDetailView.as_view(), name='casa_detail'),
] 
