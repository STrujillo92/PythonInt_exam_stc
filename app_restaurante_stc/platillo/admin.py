from django.contrib import admin

from platillo.models import Platillo

# Register your models here.
@admin.register(Platillo)
class PlatilloAdmin(admin.ModelAdmin):
    pass