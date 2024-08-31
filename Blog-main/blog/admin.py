from django.contrib import admin
from .models import Hobbies, SeriesFavoritas

@admin.register(Hobbies)
class HobbiesModelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'inicio', 'descricao']


@admin.register(SeriesFavoritas)
class HobbiesModelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'inicio', 'descricao']