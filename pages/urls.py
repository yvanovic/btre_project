from django.urls import path
from . import views  # url that is attached to a view file

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),

]
