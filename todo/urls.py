from django.urls import path
from . import views

urlpatterns = [
    path('', views.eventlist, name="Event"),
    path('create', views.eventcreate, name='create'),

]
