from xml.dom.minidom import Document
from django.template import Template, Context, loader
from django.http import HttpResponse

from web_familiares.models import Familiares

def saludo(request):
    return HttpResponse("Hola django coder")

def mi_template(request):

    plantilla =loader.get_template('index.html')

    documento = plantilla.render()

    return HttpResponse(documento)

# def familia(request):

#     nombre = ["Miguel","Damian","Pepe"]
#     apellido = ["Romero","Sanchez","Perez"]
#     dni = [20,35,33]
#     nacimiento = ["1956-03-04","1965-04-12","1989-08-15"]

#     familiar = Familiares(nombres= nombre , apellido= apellido, dni= dni , fecha_nacimiento=nacimiento)
#     familiar.save()
#     for n in range(3):
#         doc_texto1 =f"Familiar -> Nombre: {familiar.nombres[n]} Apellido: {familiar.apellido[n]} DNI: {familiar.dni[n]} fecha de nacimiento: {familiar.fecha_nacimiento[n]}"

#     return HttpResponse(doc_texto1)

def familiar(request):

    familiar = Familiares(nombres= "Miguel" , apellido= "Romero", dni= "20344311" , fecha_nacimiento="1956-03-04")
    familiar.save()
    familiar2 = Familiares(nombres= "Damian" , apellido= "Sanchez", dni= "35066433" , fecha_nacimiento="1965-04-12")
    familiar2.save()
    familiar3 = Familiares(nombres= "Pepe" , apellido= "Perez", dni= "33677733" , fecha_nacimiento="1989-08-15")
    familiar3.save()

    doc_texto =f"Familiar -> Nombre: {familiar.nombres} Apellido: {familiar.apellido} DNI: {familiar.dni} fecha de nacimiento: {familiar.fecha_nacimiento} \n Familiar -> Nombre: {familiar2.nombres} Apellido: {familiar2.apellido} DNI: {familiar2.dni} fecha de nacimiento: {familiar2.fecha_nacimiento} \n Familiar -> Nombre: {familiar3.nombres} Apellido: {familiar3.apellido} DNI: {familiar3.dni} fecha de nacimiento: {familiar3.fecha_nacimiento}"
    
    return HttpResponse(doc_texto)