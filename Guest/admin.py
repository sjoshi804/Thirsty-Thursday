from django.contrib import admin
from django.contrib.auth.admin import GuestAdmin
from .models import Guest
# Register your models here.

admin.site.register(Guest, GuestAdmin)
