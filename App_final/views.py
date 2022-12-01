from django.shortcuts import render
from django.http import HttpResponse
from App_final.forms import autoForm

from .models import Auto, Motos, Pickup_suv

# Create your views here.

def auto(requets):
    auto1=Auto(marca="fiat" ,patente="314" ,modelo="punto")
    auto1.save()
    cadena="Auto nuevo: " + auto1.marca +" "+ auto1.modelo + " con patente " + str(auto1.patente) 
    return HttpResponse (cadena)

def moto(request):
    moto1=Motos(marca="dukati" , cilindrada="250" , tipo="enduro")
    moto1.save()
    cadena="nueva moto :" + moto1.marca + " con una cilindrada de " + moto1.cilindrada+ " de tipo " +moto1.tipo
    return HttpResponse(cadena)

def pickup_suv(request):
    camioneta1=Pickup_suv(marca="Jeep" ,tipo_motor="diesel" , rodado="17" )
    camioneta1.save()
    cadena="nueva camioneta :" + camioneta1.marca + " con un motor tipo " + camioneta1.tipo_motor + " y un rodado de " + camioneta1.rodado
    return HttpResponse(cadena)

def inicio(request):
    return render(request ,"App_final/inicio.html")

def auto(request):
  
    return render (request, "App_final/auto.html")

def moto(request):
    return render(request ,"App_final/moto.html")

def pickup_suv(request):
    return render(request,"App_final/pickup_suv.html")



def autoFormulario(request):
    if request.method=="POST":
        form=autoForm(request.POST)

        if form.is_valid():
            informacion=form.cleaned_data

            marca1=informacion["marca"]
            modelo1=informacion["modelo"]
            patente1=informacion["patente"]
            auto_nuevo=Auto(marca=marca1 ,modelo=modelo1 , patente=str(patente1))
            auto_nuevo.save()
            return render(request ,"App_final/inicio.html")
    else:
        formulario=autoForm()

    return render(request ,"App_final/autoFormulario.html", {"form":formulario})

