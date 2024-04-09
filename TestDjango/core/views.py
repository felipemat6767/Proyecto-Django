from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import Usuario, UsuarioAdmin
from .forms import VehiculoForm
# Create your views here.

def home(request):
    lista = ["Inicio","Foro","Direccion" ,"Registro" ,"Inicio de Sesion"]   
    contexto = {  "lista":lista } 
    return render(request, 'core/home.html', contexto )

@login_required
def Registro_usuarios(request):  
    datos = {'form':VehiculoForm() } 
    if request.method== 'POST': 
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
    else:   
        datos['mensaje'] = "Guar Correctamente"     
    return render(request, 'core/Registro_usuarios.html', datos) 


def iniciarSesiones(request): 
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'core/Registro_usuarios.html')  
        ...
    else:
        # Return an 'invalid login' error message. 
        return render(request, 'core/inicioSesion.html') 
         