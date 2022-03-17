from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


# 
from .managers import UserManager

# Create your models here.

# con esta class vamos a reutilizar la base de django sobre user, agregandole mas parametros y permisos a los users
class User(AbstractBaseUser, PermissionsMixin):
    # aqui declaramos la seleccion que va a tener la variable genero, por el choices agregado
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),

    )
    
    # aqui creamos los campos de la base de datos
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    nombres = models.CharField(max_length=100, blank=True)    
    genero = models.CharField(max_length=1, choices = GENDER_CHOICES, blank=True)
    codregistro = models.CharField(max_length=6, blank=True)
    date_birth = models.DateField(
        'Fecha de nacimiento',
        blank=True,
        null=True,
    )
    
    # todo aquel q se registre por definicion no sera staff (False)
    is_staff = models.BooleanField(default=False)    
    is_active = models.BooleanField(default=False)
    
    # necesitamos decirle a django con que se hara el login
    USERNAME_FIELD = 'email'
    
    # para que la consola nos pida el email ya que es obligatorio para crear el usuario
    # despues de la , podemos seguir agregando parametros para q nos lo pida por consola y sea de manera obligatoria
    REQUIRED_FIELDS = ['username',] 
    
    objects = UserManager()

    # funcion para nombre corto
    def get_short_name(self):
        return self.username
    
   