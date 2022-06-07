from itertools import count
import requests

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as user_login
from django.contrib.auth.decorators import login_required, permission_required
from .models import * 
from .forms import *

# Create your views here.
@login_required
def base(request):
    return render(request, 'app/base.html')
@login_required
def cliente(request):
    return render(request, 'app/cliente.html')
@login_required
def contrato(request):
    return render(request, 'app/contrato.html')
@login_required
def deposito(request):
    return render(request, 'app/deposito.html')
@login_required
def estado(request):
    return render(request, 'app/estado.html')
@login_required
def monto(request):
    return render(request, 'app/monto.html')
@login_required
def perfil(request):
    return render(request, 'app/perfil.html')
@login_required
def reporte(request):
    return render(request, 'app/reporte.html')

# CRUD DE USER
def registro(request):
    datos = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            user_login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="cliente")
        datos["form"] = formulario
    return render(request, 'registration/registro.html', datos)
@login_required
def login(request):
    messages.success(request, "Has iniciado correctamente")
    return render(request, 'registration/login.html')
