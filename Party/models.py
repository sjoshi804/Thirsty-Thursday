from django.db import models
# Create your models here.

class Party(models.Model):   
    #Unique Party identifier
    partyid = models.CharField(max_length = 100, blank = False, null = False, unique = True, primary_key = True)

    #Basic Details
    createdAt = models.DateTimeField(auto_now_add = True)
    eventName = models.CharField(max_length = 100, blank = False, default = "Thursty Party")
    hostedBy = models.CharField(max_length = 100, blank = False)
    hostedByNameCache = models.CharField(max_length = 100, blank = False) #Put organization name here
    time = models.DateTimeField(null = False)
    location = models.CharField(max_length = 100, blank = False, null = False)

    #Status
    status = models.CharField(max_length = 20, blank = False, default = "Upcoming",)

    class Meta:
        ordering = ('time',)
