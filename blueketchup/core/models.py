from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

class AuditModel(models.Model):
    # created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Fecha de Creación")
    # updated_date = models.DateTimeField(auto_now = True, null=True, blank=True, verbose_name="Fecha de Última Modificación" )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Tag(AuditModel):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    # modified_by = models.ForeignKey(User, null=True, related_name = 'tag_id', blank=True, verbose_name="Modificado por")
    # created_by = models.ForeignKey(User, null=True, blank=True, verbose_name="Creado por")
    #franchise = models.ManyToManyField(Franchise, 'tag_id')
    #profiles = models.ManyToManyField(Profile, 'tag_id')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Etiquetas"
        verbose_name = "Etiqueta"

class Franchise(AuditModel):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.CharField(max_length=50, verbose_name="Descripción")
    tags = models.ManyToManyField(Tag, 'franchise_id', verbose_name="Etiquetas")
    # created_by = models.ForeignKey(User, null=True, verbose_name="Creado por")
    #restaurants = models.OneToManyField(Restaurant, 'franchise')
    #profiles = models.ManyToManyField(Profile, 'franchise_id')
    class Meta:
        verbose_name_plural = "Franquicias"
        verbose_name = "Franquicia"

class Profile(AuditModel):
    users = models.ManyToManyField(User, 'profile_id', verbose_name="Usuarios")
    tags = models.ManyToManyField(Tag, 'profile_id', verbose_name="Etiquetas")
    franchises = models.ManyToManyField(Franchise, 'profile_id', verbose_name="Franquisias")
    # created_by = models.ForeignKey(User, null=True, verbose_name="Creado por")

    class Meta:
        verbose_name_plural = "Perfiles"
        verbose_name = "Perfil"


class Restaurant(AuditModel):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    franchise = models.ForeignKey(Franchise, null=True, blank=True, verbose_name="Franquicia")
    latitude = models.FloatField(verbose_name="Latitud")
    longitude = models.FloatField(verbose_name="Longitud")
    description = models.TextField(max_length=150, verbose_name="Descripción")
    reference = models.TextField(max_length=100, verbose_name="Dirección")
    phone = models.TextField(max_length=20, verbose_name="Teléfono")
    tags = models.ManyToManyField(Tag, 'restaurant_id', verbose_name="Etiquetas")
    profiles = models.ManyToManyField(Profile, 'restaurant_id', blank=True, verbose_name="PErfiles")
    # created_by = models.ForeignKey(User, null=True, blank=True, verbose_name="Creado por")

    class Meta:
        verbose_name_plural = "Restaurantes"
        verbose_name = "Restaurante"



class User(User):

    sex = models.CharField(
        max_length=2,
        choices=(('M', "Masculino"), ('F', 'Femenino')),
        default='F',
    )
    profiles = models.ManyToManyField(Profile, 'user_id', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Usuarios"
        verbose_name = "Usuario"


class Dish(AuditModel):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    franchise = models.ForeignKey(Franchise, null=True, blank=True, verbose_name="Franquicia")
    restaurant = models.ForeignKey(Restaurant, null=True, blank=True, verbose_name="Restaurant")
    tags = models.ManyToManyField(Tag, 'dish_id', verbose_name="Etiquetas")
    #created_by = models.ForeignKey(User, null=True, blank=True, verbose_name="Creado por")
    #profiles = models.ManyToManyField(Profile, 'dish_id')

    class Meta:
        verbose_name_plural = "Platos"
        verbose_name = "Plato"
