from django.conf.urls import url
from todo import api

urlpatterns = [
    #GET, POST, DELETE
    url('tutorials', api.tutorial_list),

    #GET, PUT, DELETE
    url('tutorials/<int:id>', api.update_tutorials),
    url('tutorials/<int:id>', api.delete_tutorials),

    #GET
    url('tutorials/published', api.tutorial_list_published),
]