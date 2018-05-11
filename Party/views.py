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
        serializer.save()
 
 
class PartyDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PartySerializer

    def get_queryset(self):
        partyName = self.request.query_params.get('partyName', None)
        queryset = Party.objects.all()
        if partyName is not None:
            queryset = queryset.filter(eventName = partyName)
        return queryset

