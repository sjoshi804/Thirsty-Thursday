from rest_framework import serializers
from User.models import User, Operator, Orgranizer
 
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('uniqueID', 'firstName', 'lastName', 'college', 'email', 'phone', 'isOperator', 'isOrganizer',
                  'goingTo', 'attended', 'universityID')

class OperatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operator
        fields = ('user', 'checkInPermissionsFor')
        
class OrgranizerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organizer
        fields = ('user', 'organizationName', 'hostedParties', 'upcomingParties', 'currentParties')
