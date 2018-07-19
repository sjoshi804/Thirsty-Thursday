from rest_framework import serializers
from Guest.models import Guest

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('guestInstanceID', 'status', 'partyID', 'userID', 'firstName', 'lastName', 'college', 'entryTime', 'exitTime', 'paymentMethod')