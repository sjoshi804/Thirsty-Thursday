from rest_framework import serializers
from Party.models import Party
 
class PartySerializer(serializers.HyperlinkedModelSerializer):
    hostedBy = serializers.HyperlinkedIdentityField(view_name="User:User-Detail")
    class Meta:
        model = Party
        fields = ('createdAt', 'hostedBy', 'partyid', 'eventName', 'time', 'location', 'status')


