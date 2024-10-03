from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import TipoUsuario, Usuario, Talla, TipoBici, FormaPago, Arriendo, TipoProducto, Producto, Estado, Reparacion, Pago, Detalle, Despacho

""" class CustomUserCreationForm(UserCreationForm):
    pass """

class TipoUsuarioForm(ModelForm):
    tipo = forms.CharField(max_length=20,
                               required=True)
    descripcion = forms.CharField(max_length=30,
                                  required=True)
    
    class Meta:
        model = TipoUsuario
        fields = ['tipo','descripcion']

class TallaForm(ModelForm):
    talla = forms.CharField(max_length=20,
                               required=True)
    
    class Meta:
        model = Talla
        fields = ['talla']

class BiciForm(ModelForm):
    tipo = forms.CharField(max_length=20,
                               required=True)
    
    class Meta:
        model = TipoBici
        fields = ['tipo']

class FormaPagoForm(ModelForm):
    forma = forms.CharField(max_length=20,
                               required=True)
    
    class Meta:
        model = FormaPago
        fields = ['forma']

class TipoProductoForm(ModelForm):
    tipo = forms.CharField(max_length=20,
                               required=True)
    
    class Meta:
        model = TipoProducto
        fields = ['tipo']

class EstadoForm(ModelForm):
    tipo = forms.CharField(max_length=20,
                               required=True)
    
    class Meta:
        model = Estado
        fields = ['tipo']

""" class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__" """

class UsuarioForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField()
    class Meta:
        model = Usuario
        fields = ('username','rut', 'id_tipo_usuario', 'password', 'confirm_password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data





        