from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano = models.IntegerField()
    paginas = models.IntegerField()
    categoria = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20)
    idioma = models.CharField(max_length=30)
    descricao = models.TextField()
    cadastrado_por = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

# Create your models here.
