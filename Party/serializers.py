from rest_framework import serializers
from Party.models import Party
 
class PartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Party
        fields = ('createdAt', 'hostedBy', 'eventName', 'time', 'location', 'attended', 'paidVenmo', 'paidCash')


