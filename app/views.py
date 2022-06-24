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
    return render(request, 'app/cliente/cliente.html')

@login_required
def contrato(request):
    return render(request, 'app/contrato/contrato.html')

@login_required
def deposito(request):
    return render(request, 'app/posible_eliminacion/deposito.html')

@login_required
def estado(request):
    return render(request, 'app/cliente/estado.html')

@login_required
def monto(request):
    return render(request, 'app/cliente/monto.html')

@login_required
def perfil(request):
    return render(request, 'app/varios/perfil.html')

@login_required
def reporte(request):
    return render(request, 'app/varios/reporte.html')

@login_required
def contratoCliente(request):
    return render(request, 'app/contrato/contratoCliente.html')

@login_required
def contratoSeguro(request):
    return render(request, 'app/contrato/contratoSeguro.html')

@login_required
def meta(request):
    return render(request, 'app/cliente/meta.html')

@login_required
def publicaciones(request):
    return render(request, 'app/varios/publicaciones.html')

@login_required
def servicioContratado(request):
    return render(request, 'app/servicios/servicioContratado.html')

@login_required
def serviciosAdicionales(request):
    return render(request, 'app/servicios/serviciosAdicionales.html')

@login_required
def agregarContrato(request):
    return render(request, 'app/contrato/agregarContrato.html')

@login_required
def listarContrato(request):
    return render(request, 'app/contrato/listarContrato.html')

@login_required
def modificarContrato(request):
    return render(request, 'app/contrato/modificarContrato.html')

# crud registro viaje
@login_required
def registroViaje(request):
    datos = {
        'form': RegistroViajeForm()
        }
    if request.method == 'POST':
        formulario = RegistroViajeForm(request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Registro agendado  correctamente!"
    return render (request,'app/registro/registroViaje.html',datos)
@login_required
def listarRegistros(request):
    registroViajeALL = RegistroViaje.objects.all()
    datos = {
        'listarRegistro' : registroViajeALL
    }
    return render (request,'app/registro/listarRegistro.html',datos)
def modificarRegistro (request, id):
    registroViaje = RegistroViaje.objects.get(id = id)
    datos = {
        'form' : RegistroViajeForm (instance = registroViaje)
     }
    if request.method == 'POST':
        formulario = RegistroViajeForm(data=request.POST, files = request.FILES, instance=registroViaje)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Registro modificado perfectamente!')
            datos['form'] = formulario 
    return render (request,'app/registro/modificarRegistro.html',datos)

def eliminarRegistro(request, id):
    registroViaje = RegistroViaje.objects.get(id=id)
    registroViaje.delete()
    return redirect(to="listarRegistro")

# SEGURO
def seguro(request):
    return render(request, 'app/seguro/seguro.html')

def agregarSeguro(request):
    datos = {
        'form' : SeguroForm()
    }

    if request.method == 'POST':
        formulario = SeguroForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Seguro guardado correctamente!') #Nuevo 2
            
    return render(request, 'app/seguro/agregarSeguro.html', datos)

def modificarSeguro(request, codigo):
    seguro = Seguro.objects.get(codigo=codigo)
    datos = {
        'form' : SeguroForm(instance=seguro)
    }

    if request.method == 'POST':
        formulario = SeguroForm(request.POST, files=request.FILES, instance=seguro)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Seguro guardado correctamente!') #Nuevo 2
            datos['form'] = formulario
            
    return render(request, 'app/seguro/modificarSeguro.html', datos)

def listarSeguro(request):
    productosAll = Seguro.objects.all()
    datos = {
        'listaSeguro' : productosAll
    }
    
    return render(request, 'app/seguro/listarSeguro.html', datos)

def eliminarSeguro(request, codigo):
    seguro = Seguro.objects.get(codigo=codigo)
    seguro.delete()

    return redirect(to="listaSeguro")
#FIN SEGURO

# CRUD REPORTE DE CURSO
@login_required
def reporte(request):
    reporteAll = ReporteCurso.objects.all()
    datos = {
        'listaReporte': reporteAll
    }
    return render(request, 'app/reporte/reporte.html', datos)

@login_required
def crearReporte(request):
    datos = {
        'form': ReporteCursoForm()
    }
    if request.method == 'POST':
        formulario = ReporteCursoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
    return render(request, 'app/reporte/crearReporte.html', datos)

@login_required
def listaReporte(request):
    reporteAll = ReporteCurso.objects.all()
    datos = {
        'listaReporte': reporteAll
    }
    
    return render(request, 'app/reporte/listaReporte.html', datos)

@login_required
def monto(request):
    reporteAll = ReporteCurso.objects.all()
    datos = {
        'listaReporte': reporteAll
    }
    return render(request, 'app/cliente/monto.html', datos)

@login_required
def modificaReporte(request, codigo):
    reporteAll = ReporteCurso.objects.get(codigo=codigo)
    datos = {
        'form' : ReporteCursoForm(instance=reporteAll)
    }

    if request.method == 'POST':
        formulario = ReporteCursoForm(request.POST, files=request.FILES, instance=reporteAll)
        if formulario.is_valid():
            formulario.save()
            datos['form'] = formulario
            
    return render(request, 'app/reporte/modificarReporte.html', datos)

@login_required
def eliminaReporte(request, codigo):
    reporteAll = ReporteCurso.objects.get(codigo=codigo)
    reporteAll.delete()

    return redirect(to="listaReporte")


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
