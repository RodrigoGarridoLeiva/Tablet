from django import forms 
from .models import Archivo

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ('nombre', 'file', 'curso_id', 'des')

        widgets={
        'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Inserte Nombre de Archivo'}),
        'des':forms.TextInput(attrs={'class':'form-control','placeholder':'Descripción para el archivo'}),
        }

