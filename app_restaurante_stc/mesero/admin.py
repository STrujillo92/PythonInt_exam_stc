from django.contrib import admin
from mesero.models import Mesero
# Register your models here.
@admin.register(Mesero)
class MeseroAdmin(admin.ModelAdmin):
    pass