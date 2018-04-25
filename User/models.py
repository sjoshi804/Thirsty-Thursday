from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    # Account Type
    isOperator = models.BooleanField(default = False)
    isOrganizer = models.BooleanField(default = False)
    
    #Party-goer fields
    goingTo = models.ManyToManyField('Organize.Party')
    attended = models.ManyToManyField('Organize.Party')
    
    #Account Details
    venmoId = models.TextField(default = "N/A")
    universityId = models.TextField(default = "N/A")

class Operator(models.Model):
    #OneToOne mapping to User
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    #Parties that the operator has checkIn priveleges for
    checkInPermissionsFor = models.ManyToManyField('Organize.Party')
    
class Organizer(models.Model):
    #OneToOne mapping to User
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    #Name of Organization that organizer hosts parties for
    organization_name = models.TextField(null = False)
    
    #Parties that have been hosted in the past
    hostedParties = models.ForeignKey('Organize.Party', on_delete=models.CASCADE, )
    
    #Parties that have been created but have not started yet
    upcomingParties = models.ForeignKey('Organize.Party', on_delete=models.CASCADE,)
    
    #Parties that are currently going on
    currentParties = models.ForeignKey('Organize.Party', on_delete=models.CASCADE,)
    
