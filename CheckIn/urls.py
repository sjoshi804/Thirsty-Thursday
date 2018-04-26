from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from CheckIn import views
 
 
urlpatterns = [
    path(r'^checkin/$', views.partyList.as_view()),
]
