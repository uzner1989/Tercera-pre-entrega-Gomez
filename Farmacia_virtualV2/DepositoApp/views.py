from django.shortcuts import render
from django.http import HttpResponse
from DepositoApp.models import Medicacion, Laboratorio,Pedidos
from DepositoApp.forms import *
# Create your views here.
def inicio(request):
    return render(request,"DepositoApp/inicio.html")

def medicacion(request):

    med1 =Medicacion(nombre="Paracetamol", laboratorio=(1))
    med1.save()

    return render(request,"DepositoApp/medicacion.html")

def laboratorio(request):
    lab1 = Laboratorio (nombre="Szabo", direccion="Avenida italia y Propios", email ="laboratorio@szabo.com")
    lab1.save()

    return render(request,"DepositoApp/laboratorio.html")

def pedidos(request):
  
    ped1 = Pedidos (laboratorio="Szabo", fechaEntrega="2023-09-24")
    ped1.save()
    
    return render(request,"DepositoApp/entregas.html")

def medicacionFormulario(request):

    if request.method== "POST":

        formulario1= FormularioMedicacion(request.POST)

        if formulario1.is_valid():
            info=formulario1.cleaned_data

            medicacion= Medicacion(nombre=info["nombre"],laboratorio=info["laboratorio"])

            medicacion.save()

            return render(request, "DepositoApp/medicacionFormulario.html")

    else:

        formulario1 = FormularioMedicacion()

    return render(request, "DepositoApp/medicacionFormulario.html",{"form1":formulario1})    


def laboratorioFormulario(request):

    if request.method== "POST":

        formulario1= FormularioLaboratorio(request.POST)

        if formulario1.is_valid():
            info=formulario1.cleaned_data

            laboratorio= Laboratorio(nombre=info["nombre"],direcion=info["direccion"],email=info["email"])

            laboratorio.save()

            return render(request, "DepositoApp/laboratorioFormulario.html")

    else:

        formulario1 = FormularioLaboratorio()

    return render(request, "DepositoApp/laboratorioFormulario.html",{"form1":formulario1})    


def pedidosFormulario(request):

    if request.method== "POST":

        formulario1= FormularioPedidos(request.POST)

        if formulario1.is_valid():
            info=formulario1.cleaned_data

            pedidos = Pedidos(laboratorio=info["laboratorio"], fechaEntrega=info["fechaEntrega"])
            pedidos.save()

            return render(request, "DepositoApp/pedidosFormulario.html")

    else:

        formulario1 = FormularioPedidos()

    return render(request, "DepositoApp/pedidosFormulario.html",{"form1":formulario1})   

def buscarPedido(request):

    return render(request, "DepositoApp/buscarPedido.html")

def resultado(request):

   pedidos_param = request.GET.get("pedidos")


   if pedidos_param:

       pedidos = Pedidos.objects.filter(laboratorio_nombre__iexact=pedidos_param)

       return render(request, "DepositoApp/resultados.html", {"pedidos": pedidos})

   else:

       respuesta = "No ingresaste número de pedido."

       return HttpResponse(respuesta)