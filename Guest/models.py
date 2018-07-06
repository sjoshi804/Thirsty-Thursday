from django.db import models

class Guest(models.Model):
    #Status
    status = models.CharField(default = "Interested", max_length = 50, blank = True)
    
    #Unique Identifiers
    guestInstanceID = models.CharField(null = False, blank = False, max_length = 50, unique = True, primary_key = True)
    partyID = models.CharField(null = False, blank = False, max_length = 20)
    userID = models.CharField(null = False, blank = False, max_length = 30)

    #Basic Information
    firstName = models.CharField(null = False, max_length = 50)
    lastName = models.CharField(null = False, max_length = 50)
    college = models.CharField(default = "UCLA", max_length = 100)

    #Guest Instance Specific Information
    entryTime = models.DateTimeField(blank = True, null = True)
    exitTime = models.DateTimeField(blank = True, null = True, default = "1970-01-01T00:00:00Z")
    paymentMethod = models.CharField(default = "Not Paid", max_length = 50, blank = True)