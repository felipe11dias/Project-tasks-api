from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome