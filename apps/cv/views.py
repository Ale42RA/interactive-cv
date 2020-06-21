from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Cv
# Create your views here.
def cv(request):
    template = loader.get_template('cv/cv.html')
    cv = Cv.objects.order_by('published_Date')[0]
    context = {
        'cv': cv,
    }
    return HttpResponse(template.render(context, request))





  
