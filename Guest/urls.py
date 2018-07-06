#-----------------------
# Purpose: Stores all urls associated with guest check in side of the app
# Author: Siddharth Joshi
# Date Created: 07/05/18
#------------------------                                                                                                                                                                                  
from django.urls import re_path
#from rest_framework.urlpatterns import format_suffix_patterns
from Guest import views

urlpatterns = [
    #GuestInstance URLs
    re_path(r'all/$', views.GuestList.as_view(), name='guest-all'),
    re_path(r'search/(?P<pk>.+)/$', views.GuestDetail.as_view(), name='guest-detail'),
    re_path(r'filter/college/(?P<pk>.+)/$', views.GuestList.as_view(), name='guest-college-details'),
    re_path(r'filter/organized-by/(?P<pk>.+)/$', views.GuestList.as_view(), name='guest-organizer-details'),
    re_path(r'checkin/(?P<pk>.+)/$', views.GuestCheckIn, name = 'guest-check-in')
]
