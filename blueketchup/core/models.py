from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class AuditModel(models.Model):
    #created_by = models.ForeignKey(User, related_name=self.__class__.__name__+"_created_by")
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now = True, null=True, blank=True )
    #modified_by = models.ForeignKey(User, related_name=self.__class__.__name__+"_modified_by")

    class Meta:
        abstract = True




class Tag(AuditModel):
    name = models.CharField(max_length=5)
    created_by = models.ForeignKey(User,null=True, related_name="tag_created_by")
    modified_by = models.ForeignKey(User, null=True,  related_name="tag_modified_by")
    #franchise = models.ManyToManyField(Franchise)
    #profiles = models.ManyToManyField(Profile)

    def save(self, *args, **kwargs):
        self.created_date = datetime.now()
        super(Tag, self).save(*args, **kwargs)

class Franchise(AuditModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    created_by = models.ForeignKey(User, null=True, related_name="franchise_created_by")
    modified_by = models.ForeignKey(User, null=True, related_name="franchise_modified_by")
    #restaurants = models.OneToManyField(Restaurant)
    #profiles = models.ManyToManyField(Profile, 'franchise_id')
    def save(self, *args, **kwargs):
        self.created_date = datetime.now()
        super(Franchise, self).save(*args, **kwargs)

class Profile(AuditModel):
    users = models.ManyToManyField(User, 'profile_id')
    tags = models.ManyToManyField(Tag, 'profile_id', )
    franchises = models.ManyToManyField(Franchise, 'profile_id')

    def save(self, *args, **kwargs):
        self.created_date = datetime.now()
        super(Profile, self).save(*args, **kwargs)


class Restaurant(AuditModel):
    name = models.CharField(max_length=50)
    franchise = models.ManyToManyField(Franchise, null=True, blank=True)
    laitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(max_length=150)
    reference = models.TextField(max_length=100)
    phone = models.TextField(max_length=20)
    tags = models.ManyToManyField(Tag, 'restaurant_id')
    profiles = models.ManyToManyField(Profile, 'restaurant_id')
    created_by = models.ForeignKey(User, related_name="profile_created_by")
    modified_by = models.ForeignKey(User, related_name="profile_modified_by")

    def save(self, *args, **kwargs):
        self.created_date = datetime.now()
        super(Restaurant, self).save(*args, **kwargs)


class User(User):
    sex = models.CharField(
        max_length=2,
        choices=(('M', "Masculino"), ('F', 'Femenino')),
        default='F',
    )
    profiles = models.ManyToManyField(Profile, 'user_id')



class Dish(AuditModel):
    name = models.CharField(max_length=50)
    franchise = models.ForeignKey(Franchise, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, null=True, blank=True)
    created_by = models.ForeignKey(User, related_name="dish_created_by")
    modified_by = models.ForeignKey(User, related_name="dish_modified_by")
    #profiles = models.ManyToManyField(Profile, 'dish_id')

    def save(self, *args, **kwargs):
        self.created_date = datetime.now()
        super(Dish, self).save(*args, **kwargs)
