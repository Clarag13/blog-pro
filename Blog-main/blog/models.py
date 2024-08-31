from django.db import models

class Profissoes(models.Model):
    nome = models.CharField('Profissão', max_length=150)
    inicio = models.DateField('Data Inicio', auto_now_add=True)
    descricao = models.TextField('Descrição', max_length=150)
    imagem = models.ImageField('Imagem', upload_to='profissoes')

    def __str__(self) -> str:
        return self.nome
    
class Passatempos(models.Model):
    nome = models.CharField('Passatempos', max_length=150)
    inicio = models.DateField('Data de inicio', auto_now_add=True)
    descricao = models.TextField('Descrição', max_length=150)
    imagem = models.ImageField('Imagem', upload_to='passatempos')

    def __str__(self) -> str:
        return self.nome