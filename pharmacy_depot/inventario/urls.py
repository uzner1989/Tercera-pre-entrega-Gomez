from django.urls import path
from inventario import views

urlpatterns = [
    path('productos/', views.producto_list, name='producto_list'),
    path('productos/<int:producto_id>/', views.producto_detail, name='producto_detail'),
]
