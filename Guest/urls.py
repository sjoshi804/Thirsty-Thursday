#-----------------------
# Purpose: Stores all urls associated with guest check in side of the app
# Author: Siddharth Joshi
# Date Created: 07/05/18
#------------------------                                                                                                                                                                                  
from django.urls import re_path
#from rest_framework.urlpatterns import format_suffix_patterns
from Guest import views

urlpatterns = [
    #Guest Instance URLs
    re_path(r'all/$', views.GuestCheckIn.as_view(), name='guest-all'),
    re_path(r'search/(?P<pk>.+)/$', views.GuestDetail.as_view(), name='guest-detail'),
    re_path(r'filter/college/(?P<pk>.+)/$', views.GuestList.as_view(), name='guest-college-details'),
    re_path(r'filter/organized-by/(?P<pk>.+)/$', views.GuestList.as_view(), name='guest-organizer-details'),
    re_path(r'attended-by/(?P<pk>.+)/$', views.GuestAttended.as_view(), name='guest-parties-attended'),
    re_path(r'party/(?P<pk>.+)/$', views.GuestList.as_view(), name='guests-for-party'),
    re_path(r'check-in/$', views.GuestCheckIn.as_view(), name = 'guest-check-in')
]
