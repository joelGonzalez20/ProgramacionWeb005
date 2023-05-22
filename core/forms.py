from django import forms
from django.forms import ModelForm
from .models import *

class formClientes(ModelForm):

    class Meta:
        model = Cliente
        fields=['rut','dv','nombre','appaterno','apmaterno','email','telefono','cargo']

class ProductoForm(ModelForm):

    nombreProducto = forms.CharField(min_length=4,widget=forms.TextInput(attrs={"placeholder":"Ingrese Nombre"}))
    precioProducto = forms.IntegerField(min_value=500,widget=forms.NumberInput(attrs={"placeholder":"Ingrese Precio"}))
    stock = forms.IntegerField(min_value=0,widget=forms.NumberInput(attrs={"placeholder":"Ingrese Stock"}))

    
    class Meta:
        model = Producto
        #fields = ['nombre','precio','stock','descripcion','tipo']
        fields = '__all__'

    