from multiprocessing import context
from django.contrib import admin
from main.models import *

class MotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'ano', 'preco')
    search_fields = ('modelo',)

admin.site.register(Moto, MotoAdmin)
admin.site.register(Base)
admin.site.register(Imagens)

