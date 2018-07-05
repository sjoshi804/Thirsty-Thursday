#-----------------------
# Purpose: Stores all urls associated with organizer side of the app
# Author: Siddharth Joshi
# Date Created: 04/18/18
#------------------------

from django.urls import re_path
#from rest_framework.urlpatterns import format_suffix_patterns
from Party import views
 
urlpatterns = [
    re_path(r'all/$', views.PartyList.as_view(), name='party-list'),
    re_path(r'search/(?P<partyid>.+)/$', views.PartyDetail.as_view(), name='party-detail'),
    re_path(r'filter/college/(?P<partyid>.+)/$', views.PartyManyDetail.as_view(), name='party-college-details'),
    re_path(r'filter/organized-by/(?P<partyid>.+)/$', views.PartyManyDetail.as_view(), name='party-organizer-details'),
]
