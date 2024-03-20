from django.http import HttpResponse
import datetime 
from django.template import Template,context
from django.template import loader


def saludar (request):
    doc_externo=open ("C:/Users/SENA/Documents/ProyectoDjango01/miPrimerProyecto/miPrimerProyecto/plantillas/miprimeraplantilla.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    cxt=Context()
    documento=plt.render (cxt)
    return HttpResponse("Hola gamer es la primera vista")

def fecha (request):
    fechaActual=datetime.datetime.now()
    documento= """<HTML>
                    <HEAD>
                    <TITLE>esta es una estrucutra basica de documento html</TITLE>
                    </HEAD>
                    <BODY>
                      <H1> Usted ingreso o actualio en la vista en lafecha %s </H1>
                    </BODY>
                 </HTML> """ %fechaActual
    return HttpResponse (documento)

def tareasEnlistadas(request):
    Tareas=["Aprender sobre la internet","Aprender html", "Aprender css", "Practicar python","Aprender Django","construir mi propia WEb"]
    doc_externo=loader.get_template("segundaplantilla.html")
    documento=doc_externo.render({"listado":Tareas})
    return HttpResponse(documento)

def games(request):
    agno=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime("%x")

    fecha="%s%s%s a las %s" %(dia,mes,agno,hora)

    doc_externo=loader.get_template("games.html")
    documento=doc_externo.render({"fecha":fecha})
    return HttpResponse(documento)

def musica(request):
    agno=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime("%x")

    fecha="%s%s%s a las %s" %(dia,mes,agno,hora)

    doc_externo=loader.get_template("musica.html")
    documento=doc_externo.render({"fecha":fecha})
    return HttpResponse(documento)

def tecnologia(request):
    agno=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime("%x")

    fecha="%s%s%s a las %s" %(dia,mes,agno,hora)

    doc_externo=loader.get_template("tecnologias.html")
    documento=doc_externo.render({"fecha":fecha})
    return HttpResponse(documento)