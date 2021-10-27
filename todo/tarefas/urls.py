from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='lista'),
    path('atualizar/<str:pk>/', views.atualizarTarefa, name="atualizar"),
    path('deletar/<str:pk>/', views.deletarTarefa, name="deletar")
]