#-----------------------
# Purpose: Stores all urls associated with user, operator and organizer side of the app
# Author: Siddharth Joshi
# Date Created: 05/08/18
#------------------------                                                                                                                                                                                  
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from User import views

urlpatterns = [
   re_path(r'^users/$', views.UserList.as_view(), name='user-list'),
   re_path(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
]
