
from django.shortcuts import render, get_object_or_404,redirect
from django.template import loader
from django.http import HttpResponse
def myIndex(request):
    #text="""<h1>Clap your hand son excellence is comming Every body evey body son excellence is comming</h1>""";
    context = {"message" : "Clap Your hand son excellence is comming Everybody every body son excellence is comming"}
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request));