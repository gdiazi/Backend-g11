from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from .models import Usuario

class SoloClientes(BasePermission):
 
     message = 'Solo los clientes pueden realzar esta petició'
 
 
def has_permission(self, request: Request, view):
  
    usuario = request.user
    
    
    
    
    if usuario.tipousuario == 'CLIENTE':
     
      return True
 
    else:
       return False
      
      
      