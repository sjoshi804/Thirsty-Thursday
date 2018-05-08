#-----------------------
# Purpose: Stores all urls associated with organizer side of the app
# Author: Siddharth Joshi
# Date Created: 04/18/18
#------------------------

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from  import views
 
urlpatterns = [
    url(r'^todos/$', views.TodoList.as_view(), name='todo-list'),
    url(r'^todos/(?P<pk>[0-9]+)/$', views.TodoDetail.as_view(), name='todo-detail'),
]
