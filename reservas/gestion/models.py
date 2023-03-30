from django.db import models

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.TextField(null=False)
    habilitado = models.BooleanField(default=True)

    class Meta:
        # sirve para modificar alguna configuracion de la tabla en nuestra BD
        db_table = 'categorias'
        
class Producto(models.Model):
    nombre = models.TextField(null=False)
    precio = models.FloatField()
    disponible = models.BooleanField(default=True)
    
    createAt = models.DateTimeField(auto_now_add=True, db_column='created_at')      
    
    updatedAt = models.DateTimeField(auto_now=True, db_column='updated_at')
    
    categoria = models.ForeignKey(to=Categoria, on_delete=models.CASCADE, db_column='categoria_id', related_name='productos')
    
    class Meta:
        db_table = 'productos'
        
        ordering = ['-nombre','precio']
        
        unique_together = ['nombre', 'precio']
        
        
    
    
        