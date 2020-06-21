from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.template import loader


# Create your views here.

def main(request):
    post_list = Post.objects.order_by('published_Date')[:5]
    template = loader.get_template('blog/blog.html')
    context = {
        'post_list': post_list,
    }
    return HttpResponse(template.render(context, request))

def postinfo(request, post_id):
    selec_post = Post.objects.filter(id=post_id)[0]
    template = loader.get_template('blog/postinfo.html')
    context = {
        'selec_post': selec_post,
    }
    return HttpResponse(template.render(context, request))

