from django import forms
from django.forms import ModelForm

from .models import *

class TarefaForm(forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Adicione uma nova tarefa aqui ...'}))

    class Meta:
        model = Tarefa
        fields = '__all__'