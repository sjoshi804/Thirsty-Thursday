from django.db import models
# Create your models here.

class User(models.Model):
    #Unique Account Identifiers
    uniqueID = models.CharField(null = False, blank = False, max_length = 30, unique = True, primary_key = True)
    universityID = models.CharField(default = "ERROR: no UID", blank = False, max_length = 20)    

    #Basic Information
    firstName = models.CharField(null = False, max_length = 50)
    lastName = models.CharField(null = False, max_length = 50)
    college = models.CharField(default = "UCLA", max_length = 100)

    #Contact Information 
    email = models.CharField(null = False, max_length = 100)
    phone = models.CharField(default = "N/A", max_length = 20)

    #Account Type
    isOperator = models.BooleanField(default = False)
    isOrganizer = models.BooleanField(default = False)
    

class Operator(models.Model):
    #OneToOne mapping to UserID and PartyID
    permissionID = models.CharField(max_length = 100, blank = False, unique = True, primary_key = True) #contains the user uniqueID
   
class Organizer(models.Model):
    #OneToOne mapping to User
    user = models.CharField(max_length = 100, blank = False, unique = True, primary_key = True) #contains the user uniqueID
    
    #Name of Organization that organizer hosts parties for
    organizationName = models.CharField(max_length = 100, blank = False)
    collegeName = models.CharField(max_length = 100, blank = True, default = "UCLA")
