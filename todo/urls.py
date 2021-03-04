from django.urls import path
from . import views

urlpatterns = [
    path('', views.eventlist, name="Event"),
    path('get/<str:pk>', views.eventDetail, name='get'),
    path('tutorials', views.eventcreate, name='tutorials'),
    path('eventupdate/<str:pk>', views.taskUpdate, name='eventupdate'),
    path('task/<str:pk>', views. taskDelete, name='task'),

]
