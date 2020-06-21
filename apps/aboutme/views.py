from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Me
from .models import Equipment
from .models import Skillset
from .models import WorkExp
from .models import Education
from .models import Attribute
from .models import Like

def aboutme(request):
    me = Me.objects.order_by('my_Level')[0]
    equipment_list = Equipment.objects.order_by('equipment_Name')
    skill_list = Skillset.objects.order_by('skill_Title')
    work_list = WorkExp.objects.order_by('year_Started')
    education_list = Education.objects.order_by('year_Gained')
    attribute_list = Attribute.objects.order_by('attribute_Name')
    like_list = Like.objects.order_by('like_Title')

    template = loader.get_template('aboutme/aboutme.html')
    context = {
        'me': me,
        'equipment_list': equipment_list,
        'skill_list': skill_list,
        'work_list': work_list,
        'education_list': education_list,
        'attribute_list': attribute_list,
        'like_list': like_list,
    }
    return HttpResponse(template.render(context, request))
# Create your views here.
