from multiprocessing import context
from django.contrib import admin
from main.models import *

class MotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'ano', 'valor_vista')
    search_fields = ('modelo',)

admin.site.register(Categoria)
admin.site.register(Moto, MotoAdmin)

