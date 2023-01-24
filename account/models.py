import random
from django.db import models
from django.contrib.auth.models import AbstractUser
from account import managers

class Employees(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'M', ('Male')
        FEMALE = 'F', ('Female')
    def generate_register_number(lenght):
        min = pow(10, lenght - 1)
        max = pow(10, lenght) - 1
        return random.randint(min, max)

    id = models.AutoField(
        primary_key=True,
        null=False,
    )
    cpf = models.CharField(
        null=False,
        unique=True,
        max_length=14,
    )
    email = models.CharField(
        db_column='tx_email',
        null=False,
        max_length=64,
        unique=True
    )
    name = models.CharField(
        'Name',
        max_length=80,
        null=False,
        blank=False,
    )
    register_number = models.CharField(
        'Register Number',
        max_length=5,
        null=False,
        blank=False,
        default=generate_register_number(5),
    )
    birth_date = models.DateField(
        'BirthDate',
        null=False,
        blank=False,
    )
    gender = models.CharField(
        'Gender',
        null=False,
        blank=False,
        max_length=1,
        choices=Gender.choices,
    )
    admission_date = models.DateField(
        'Admission Date',
        null=False,
        blank=False,
    )
    address = models.CharField(
        'Adress',
        max_length=80,
        null=False,
        blank=False,
    )
    neighborhood = models.CharField(
        'Neighborhood',
        max_length=80,
        null=False,
        blank=False,
    )
    city = models.CharField(
        'City',
        max_length=80,
        null=False,
        blank=False,
    )
    post_code = models.CharField(
        'Post Code',
        max_length=15,
        null=False,
        blank=False,
    )
    state = models.CharField(
        'State',
        max_length=2,
        null=False,
        blank=False,
    )
    phone = models.IntegerField(
        'Phone',
        null=False,
        blank=False,
    )
    id_role = models.ForeignKey(
        'core.Role',
        related_name='employee_role',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    id_association = models.ForeignKey(
        'core.EmploymentAssociation',
        related_name='employee_bond',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
        
    objects = managers.UsersManager()
    
    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self) -> str:
        return self.email
     
    class Meta:
        db_table = 'tb_employees'