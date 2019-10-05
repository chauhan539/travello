from django.urls import path
from . import views

# below are the calling method of a urls name

urlpatterns = [

    path('', views.index, name='index')

]
