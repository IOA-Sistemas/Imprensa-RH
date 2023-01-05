from django.db import models
from django.contrib.auth.models import AbstractUser
from account import managers

class User(AbstractUser):
    id = models.AutoField(
        primary_key=True,
        null=False,
    )
    username = models.CharField(
        db_column='tx_username',
        null=False,
        max_length=64,
        unique=True
    )
    
    email = models.CharField(
        db_column='tx_email',
        null=False,
        max_length=64,
        unique=True
    )
    
    objects = managers.UsersManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self) -> str:
        return self.username