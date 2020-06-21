from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

def contactme(request):
    template = loader.get_template('contactme/contactme.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
