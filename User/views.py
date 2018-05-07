from User.models import User, Operator, Organizer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from User.serializers import UserSerializer, OperatorSerializer, OrganizerSerializer
 
 
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
 
 
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.all().filter(user=self.request.user)

 
class OperatorList(generics.ListCreateAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer
 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
 
 
class OperatorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OperatorSerializer
    
    def get_queryset(self):
        return Operator.objects.all().filter(user=self.request.user)
 
class OrganizerList(generics.ListCreateAPIView):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer
 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
 
 
class OrgranizerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrganizerSerializer
    
    def get_queryset(self):
        return Organizer.objects.all().filter(user=self.request.user)
