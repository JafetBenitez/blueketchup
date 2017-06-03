from django.contrib import admin
from core import models
# Register your models here.
admin.site.register(models.Tag)
admin.site.register(models.Profile)
admin.site.register(models.Franchise)
admin.site.register(models.Restaurant)
admin.site.register(models.Dish)
