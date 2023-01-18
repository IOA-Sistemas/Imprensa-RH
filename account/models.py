from django.db import models
from django.contrib.auth.models import AbstractUser
from account import managers
import re
from django.core.exceptions import ValidationError

class User(AbstractUser):
    def validate_cpf(value):
        if not re.match(r'([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})', value):
            raise ValidationError('CPF/CNPJ inválido')
    
    username = None
    id = models.AutoField(
        primary_key=True,
        null=False,
    )
    cpf = models.IntegerField(
        null=False,
        unique=True,
        max_length=14,
        validators=[validate_cpf]
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
        return self.email
     
    class Meta:
        db_table = 'user_auth'