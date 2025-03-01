from django.urls import path
from .views import home_view, list_view, delete_view, detail_view, update_view, register_view

app_name = 'site'
urlpatterns = [
    path('', home_view, name='home'),
    path('cadastro/', register_view, name='criar'),
    path('listar/', list_view, name='listar'),
    path('detalhes/<int:pk>/', detail_view, name='detalhe'),
    path('atualizar/<int:pk>/', update_view, name='atualizar'),
    path('deletar/<int:pk>/', delete_view, name='deletar'), 
]
