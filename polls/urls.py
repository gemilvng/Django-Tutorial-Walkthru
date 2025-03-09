# This file is reference to anything want to access features in polls/
# "From ." means importing form the same directory. Wow, it is a file-as-a-module concept (?)
from django.urls import path
from . import views

# urlpatterns defined as a list data type
# "" as in the first argument means the root directory
urlpatterns = [
    path("", views.index, name="index"),
]