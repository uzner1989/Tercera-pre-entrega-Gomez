from django import forms
from .models import Producto, Cliente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'direccion', 'telefono']


class BuscarForm(forms.Form):
   
    nombre = forms.CharField(label='Nombre', max_length=100, required=False)
    categoria = forms.ChoiceField(label='Categoría', choices=[('', 'Todas las categorías')], required=False)
    fecha = forms.DateField(label='Fecha', required=False)

    def __init__(self, categorias, *args, **kwargs):
        super(BuscarForm, self).__init__(*args, **kwargs)
       
        self.fields['categoria'].choices += [(c, c) for c in categorias]