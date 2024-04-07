from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.UserLogins)
admin.site.register(models.UserDevice)
admin.site.register(models.UserIP)
