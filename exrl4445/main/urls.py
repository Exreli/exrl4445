from django.urls import path

from .views import *

urlpatterns = [
    path('', input_form, name='input_form'),
    path('add_arguments_to_db', add_arguments_to_db, name='add_arguments_to_db'),
    path('arguments', ArgumentsList.as_view(), name='arguments'),
]
