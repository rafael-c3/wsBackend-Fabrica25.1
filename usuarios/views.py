from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def home_view(request):
    return render(request, 'site/home.html')

def register_view(request):
    if request.method == 'GET':
        form = UsuarioForm()
        return render(request, 'site/cadastro.html', {'form': form})
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('site:listar')

def list_view(request):
    usuarios = Usuario.objects.all()
    if usuarios:
        return render(request, 'site/listar.html', {'usuarios': usuarios})
    return render(request, 'site/listar.html')

def detail_view(request, pk):
    usuario = Usuario.objects.get(pk = pk)
    if usuario:
        return render(request, 'site/detail.html', {'usuario': usuario})
    
def delete_view(request, pk):
    usuario = Usuario.objects.get(pk = pk)
    if usuario:
        usuario.delete()
        request.status_code = 204
        return redirect('site:listar')

def update_view(request, pk):
    usuario = Usuario.objects.get(pk = pk)
    if request.method == 'GET':
        form = UsuarioForm(instance = usuario)
        return render(request, 'site/update.html', {'usuario': usuario, 'form': form})
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance = usuario)
        if form.is_valid():
            form.save()
            return redirect('site:listar')
        
    
                