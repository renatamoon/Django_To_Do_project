from django.db import models

# Create your models here.

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    completo = models.BooleanField(default=False) #não será completado
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo