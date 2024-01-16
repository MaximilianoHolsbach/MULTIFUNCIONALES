from django import forms



class ClienteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    telefono = forms.IntegerField(label="Telefono", )
    email = forms.CharField(label="Email", max_length=100)

class TecnicoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    telefono = forms.IntegerField(label="Telefono", )
    email = forms.CharField(label="Email", max_length=100)

class EquipoForm(forms.Form):
    modelo = forms.CharField(label="Nombre", max_length=100)
    serie = forms.CharField(label="Apellido", max_length=100)
    fecha_ingreso = forms.DateField(label="Feha de ingreso", )