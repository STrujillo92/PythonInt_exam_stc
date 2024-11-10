from django.contrib import admin
from comensal.models import Comensal
# Register your models here.
@admin.register(Comensal)
class ComensalAdmin(admin.ModelAdmin):
    pass