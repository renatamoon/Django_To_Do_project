from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    tarefas = Tarefa.objects.all()

    form = TarefaForm()

    if request.method =='POST':
        form = TarefaForm(request.POST) #salvando o formulario de tarefas
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tarefas':tarefas, 'form':form}
    return render(request, 'tarefas/lista.html', context)


def atualizarTarefa(request, pk):
    tarefa = Tarefa.objects.get(id=pk)

    form = TarefaForm(instance=tarefa)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'tarefas/atualizar.html', context)

def deletarTarefa(request, pk):
    item = Tarefa.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'tarefas/deletar.html', context)