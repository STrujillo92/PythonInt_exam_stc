from django.forms import ModelForm
from mesero.models import Mesero

class MeseroForm(ModelForm):
    class Meta:
        model = Mesero
        fields = ('nombre','nacionalidad','edad','dni')