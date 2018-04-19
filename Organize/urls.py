#-----------------------
# Purpose: Stores all urls associated with organizer side of the app
# Author: Siddharth Joshi
# Date Created: 04/18/18
#------------------------

from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name = 'index'),
]
