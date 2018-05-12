#-----------------------
# Purpose: Stores all urls associated with user, operator and organizer side of the app
# Author: Siddharth Joshi
# Date Created: 05/08/18
#------------------------                                                                                                                                                                                  
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from User import views

urlpatterns = [
   re_path(r'all/$', views.UserList.as_view(), name='user-list'),
   re_path(r'search/(?P<id>)/$', views.UserDetail.as_view(), name='user-detail'),
   re_path(r'filter/college/(?P<college>)/$', views.UserCollege.as_view(), name='user-college-detail'),
]
