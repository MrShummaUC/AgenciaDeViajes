from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Creamos un template del formulario
class SeguroForm (forms.ModelForm):

    class Meta: 
        model = Seguro
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email','password1','password2']

class ReporteCursoForm(forms.ModelForm):
    class Meta:
        model = ReporteCurso
        fields = '__all__'

class ReporteCursoForm(forms.ModelForm):
    class Meta:
        model = ReporteCurso
        fields = '__all__'

class RegistroViajeForm(ModelForm):
    class Meta:
        model = RegistroViaje
        fields = ['id','clienteCorreo','destinoCorreo','nAlumnos','tipo','fechaViaje','tipoActividad','datoRelevante']

class ContratoCursoForm(forms.ModelForm):
    class Meta:
        model = ContratoCurso
        fields = '__all__'                