from django.db import models

class Hobbies(models.Model):
    nome = models.CharField('Hobbie', max_length=150)
    inicio = models.DateField('Data Inicio', auto_now_add=True)
    descricao = models.TextField('Descrição', max_length=150)
    imagem = models.ImageField('Imagem', upload_to='hobbies')

    def __str__(self) -> str:
        return self.nome
    
class SeriesFavoritas(models.Model):
    nome = models.CharField('Series Favoritas', max_length=150)
    inicio = models.DateField('Data de inicio', auto_now_add=True)
    descricao = models.TextField('Descrição', max_length=150)
    imagem = models.ImageField('Imagem', upload_to='series')

    def __str__(self) -> str:
        return self.nome