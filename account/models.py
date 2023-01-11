from django.db import models
from django.contrib.auth.models import AbstractUser
from account import managers

class User(AbstractUser):
    id = models.AutoField(
        primary_key=True,
        null=False,
    )
    cpf = models.IntegerField(
        null=False,
        unique=True
    )
    email = models.CharField(
        db_column='tx_email',
        null=False,
        max_length=64,
        unique=True
    )
    
    objects = managers.UsersManager()
    
    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self) -> str:
        return self.username
    
    class Meta:
        db_table = 'user_auth'