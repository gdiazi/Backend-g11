from django.urls import path
from .views import *




urlpatterns = [
      path('prueba', PruebaView.as_view()),
      path('otra_prueba', PruebaView.as_view()),
      path('categorias', CategoriaView.as_view()),
      path('categorias/<int:id>', UnaCategoriaView.as_view()),
      path('productos', ProductosView.as_view()),
      path('productos-generic', ProductosGenericView.as_view()),      
      path('producto/<int:id>', UnProductoView.as_view()),

]
  