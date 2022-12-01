from django.urls import path
from App_final.views import *

urlpatterns =[
    path("auto/", auto, name="auto"),
    path("moto/", moto, name="moto"),
    path("pickup_suv/", pickup_suv, name="pickup_suv"),
    path("", inicio, name="inicio"),
    path("autoFormulario/", autoFormulario , name="autoFormulario"),



]   