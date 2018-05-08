from django.db import models
# Create your models here.

class User(models.Model):
    #Unique Account Indentifier
    uniqueID = models.TextField(null = False)
    
    #Basic Information
    firstName = models.TextField(null = False)
    lastName = models.TextField(null = False)
    college = models.TextField(default = "UCLA")

    #Contact Information 
    email = models.TextField(null = False)
    phone = models.TextField(default = "N/A")

    # Account Type
    isOperator = models.BooleanField(default = False)
    isOrganizer = models.BooleanField(default = False)
    
    #Party-goer fields
    goingTo = models.ManyToManyField('Party.Party', related_name = '%(class)s_goingTo')
    attendedParties = models.ManyToManyField('Party.Party', related_name = '%(class)s_attenededParties')
    
    #Account Details
    universityID = models.TextField(default = "N/A")

class Operator(models.Model):
    #OneToOne mapping to User
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    #Parties that the operator has checkIn priveleges for
    checkInPermissionsFor = models.ManyToManyField('Party.Party', related_name = '%(class)s_permissions')
    
class Organizer(models.Model):
    #OneToOne mapping to User
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    #Name of Organization that organizer hosts parties for
    organizationName = models.TextField(null = False)
    
    #Parties that have been hosted in the past
    hostedParties = models.ForeignKey('Party.Party', on_delete=models.CASCADE, related_name = '%(class)s_hostedParties')
    
    #Parties that have been created but have not started yet
    upcomingParties = models.ForeignKey('Party.Party', on_delete=models.CASCADE, related_name = '%(class)s_upcomingParties')
    
    #Parties that are currently going on
    currentParties = models.ForeignKey('Party.Party', on_delete=models.CASCADE, related_name = '%(class)s_currentParties')
    
