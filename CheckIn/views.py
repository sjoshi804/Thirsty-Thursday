from django.shortcuts import render
from Organize.models import Party
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
# Create your views here.

from Organize.serializers import PartySerializer

class PartyList (generics.ListCreateAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
