from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def main(request):
    template = loader.get_template('portfolio/portfolio.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


