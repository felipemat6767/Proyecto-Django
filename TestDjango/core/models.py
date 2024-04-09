from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length = 300, primary_key=True, verbose_name="Nombre de Usuario")
    contraseña = models.CharField(max_length = 100, verbose_name="Contraseña")  
    email = models.CharField(max_length = 100, unique = True )
    
    
    def __str__(self):
        return self.nombre 
    
class UsuarioAdmin(models.Model):
    nombre = models.CharField(max_length = 300, unique = True)
    contraseña = models.CharField(max_length = 100 )
    email = models.CharField(max_length = 100, unique = True )
    
    
    def __str__(self):
        return self.nombre     