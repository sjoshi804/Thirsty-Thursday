#-----------------------
# Purpose: Stores all urls associated with organizer side of the app
# Author: Siddharth Joshi
# Date Created: 04/18/18
#------------------------

from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from Party import views
 
urlpatterns = [
    re_path(r'$', views.PartyList.as_view(), name='party-list'),
    re_path(r'(?P<partyid>.+)/$', views.PartyDetail.as_view(), name='party-detail'),
]
