from django.db import models
# Create your models here.

class Party(models.Model):
    createdAt = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length = 100, blank = False, default = "Thursty Party")
    organizer = models.ForeignKey(User, related_name = 'parties', on_delete = models.CASCADE, null = False)
    class Meta:
        ordering = ('createdAt',)

