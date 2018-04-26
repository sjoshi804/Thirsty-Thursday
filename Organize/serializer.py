from rest_framework import serializers
 
from Organize.models import Party
 
class PartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Party
        fields = ('createdAt', 'eventName', 'time', 'location')


