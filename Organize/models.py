from django.db import models
# Create your models here.

class Party(models.Model):
    createdAt = models.DateTimeField(auto_now_add = True)
    eventName = models.CharField(max_length = 100, blank = False, default = "Thursty Party")
#   hostedBy = models.ForeignKey(User, related_name = 'parties', on_delete = models.CASCADE, null = False)
    time = models.DateTimeField(null = False)
    location = models.CharField(max_length = 100, blank = False, null = False)
#   paidVenmo = models.ForeinKey or manyToMany?
#   paidCash = models.ForeignKey or manyToMany?
#   attended = models.ForeignKey or ManyToMany?
    class Meta:
        ordering = ('time',)


 

