from rest_framework import serializers
from User.models import User, Operator, Organizer
 
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('uniqueID', 'firstName', 'lastName', 'college', 'email', 'phone', 'isOperator', 'isOrganizer',
                 """ 'goingTo', 'attendedParties',""" 'universityID')

class OperatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operator
        fields = ('user', 'checkInPermissionsFor')
        
class OrganizerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organizer
        fields = ('user', 'organizationName', 'hostedParties', 'upcomingParties', 'currentParties')
