from django import forms

class FormularioMedicacion(forms.Form):
    nombre =forms.CharField(max_length=40)
    laboratorio =forms.IntegerField()

class FormularioLaboratorio(forms.Form):
    nombre= forms.CharField()
    direccion= forms.CharField()
    email = forms.EmailField()

class FormularioPedidos(forms.Form):
    laboratorio = forms.CharField()
    fechaEntrega= forms.DateField()