from django.db import models
# Create your models here.

class Party(models.Model):
    id = models.TextField(max_length = 10, blank = False, null = False)
    createdAt = models.DateTimeField(auto_now_add = True)
    eventName = models.CharField(max_length = 100, blank = False, default = "Thursty Party")
    
    hostedBy = models.ForeignKey('User.Organizer', related_name = 'parties', on_delete = models.CASCADE, null = False)
    time = models.DateTimeField(null = False)
    location = models.CharField(max_length = 100, blank = False, null = False)
    
    #Guest List
    attended = models.ManyToManyField('User.User')
    paidVenmo = models.ManyToManyField ('User.User')
    paidCash = models.ManyToManyField('User.User')

    class Meta:
        ordering = ('time',)
