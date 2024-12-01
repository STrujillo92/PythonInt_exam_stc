from django.forms import ModelForm
from platillo.models import Platillo

class PlatilloForm(ModelForm):
    class Meta:
        model = Platillo
        fields = ('nombre','precio','procedencia')