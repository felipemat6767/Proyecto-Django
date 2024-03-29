from django.shortcuts import render

# Create your views here.

def home(request):
    lista = ["Inicio","Foro","Direccion" ,"Registro" ,"Inicio de Sesion"]  
    contexto = {"nombre":"Felipe", "lista":lista} 
    return render(request, 'core/home.html', contexto )

