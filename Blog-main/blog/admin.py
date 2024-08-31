from django.contrib import admin
from .models import Profissoes, Passatempos

@admin.register(Profissoes)
class ProfissoesModelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'inicio', 'descricao']


@admin.register(Passatempos)
class PassatemposModelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'inicio', 'descricao']