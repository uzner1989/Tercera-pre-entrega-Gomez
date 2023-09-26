from django.urls import path, include
from DepositoApp.views import *
urlpatterns = [


    path("",inicio, name="Inicio"),
    path("medicacion/", medicacion, name= "Medicacion"),
    path("laboratorio/", laboratorio, name="Laboratorio"),
    path("entregas/", pedidos, name="Pedidos"),
    path("laboratorioFormulario/", laboratorioFormulario, name="LaboratorioFormulario"),
    path("medicacionFormulario/", medicacionFormulario, name="MedicacionFormulario"),
    path("pedidosFormulario/", pedidosFormulario, name="PedidosFormulario"),
    path("resultados/",resultado, name="ResultadosBusqueda"),
    path("buscarPedido/", buscarPedido, name="BuscarPedido")

]
    