from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.main, name='index'),
    path('<int:post_id>/', views.postinfo, name='postinfo'),

]