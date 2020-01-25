from django.contrib import admin
from .models import Biblioteca
# Register your models here.
class LibraryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
admin.site.register(Biblioteca)