#-----------------------
# Purpose: all views associated with organizer's side of the app
# Author: Siddharth Joshi
# Date Created: 04/18/18
#------------------------
from Party.models import Party
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from Party.serializers import PartySerializer
 
 
class PartyList(generics.ListCreateAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
 
 
class PartyDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PartySerializer
    
    def get_queryset(self):
        return Party.objects.all().filter(user=self.request.user)

