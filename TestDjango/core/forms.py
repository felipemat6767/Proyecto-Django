from django import forms 
from .models import Usuario  

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nombre","contraseña","email"] 