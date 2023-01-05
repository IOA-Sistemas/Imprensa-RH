from django.db import models
import random
from account.models import User

# Table cargo
class Role(models.Model):
    class Scholarity(models.TextChoices):
        MEDIO_INCOMPLETO = 'MI', ('Ensino Médio Incompleto')
        MEDIO_COMPLETO = 'MC', ('Ensino Médio Completo')
        SUPERIOR_INCOMPLETO = 'SI', ('Superior Incompleto')
        SUPERIOR_COMPLETO = 'SC', ('Superior Completo')
        MESTRADO = 'M', ('Mestrado'),
        DOUTORADO = 'D', ('Doutorado')
    
    role_name = models.CharField(
        'Role Name',
        max_length=80,
        null=False,
        blank=False,
    )
    salary = models.FloatField(
        'Salary',
        null=False,
        blank=False,
    )
    scholarity = models.CharField(
        'Scholarity',
        max_length=2,
        null=False,
        blank=False,
        choices=Scholarity.choices,
    )
    graduation = models.CharField(
        'Graduation',
        null=True,
        blank=True,
        max_length=80,
    )
    role_description = models.TextField(
        'Role Description',
        null=False,
        blank=False,
    )
    
    def __str__(self) -> str:
        return self.role_name

# Table departamento
class Departament(models.Model):
    departament_name = models.CharField(
        'Departament Name',
        max_length=80,
        null=False,
        blank=False,
    )
    description = models.CharField(
       'Departament Description',
        max_length=200,
        null=True,
        blank=True,
    )
    
    def __str__(self) -> str:
        return self.departament_name

# Table vinculo
class EmploymentBond(models.Model):
    class Type(models.TextChoices):
        CLT = 'C', ('CLT')
        PJ = 'P', ('PJ')
        TRAINEE = 'T', ('Trainee')
    
    type = models.CharField(
        'Type of Employment Bond',
        max_length=200,
        null=False,
        blank=False,
        choices=Type.choices,
    )
    description = models.CharField(
        'Description',
        max_length=80,
        null=True,
        blank=True,
    )
    
    def __str__(self) -> str:
        return self.type


# Table servidor
class Employee(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', ('Male')
        FEMALE = 'F', ('Female')
    
    def generate_register_number(lenght):
        min = pow(10, lenght - 1)
        max = pow(10, lenght) - 1
        return random.randint(min, max)
    
    user = models.ForeignKey(
        User,
        related_name='user_account',
        on_delete=models.CASCADE,
        null=False,
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
    email = models.EmailField(
        'Email',
        max_length=80,
        null=False,
        blank=False,
    )
    id_role = models.ForeignKey(
        Role,
        related_name='employee_role',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    id_bond = models.ForeignKey(
        EmploymentBond,
        related_name='employee_bond',
        on_delete=models.CASCADE,
        null=True,
        blank=False,
    )
    
    def __str__(self) -> str:
        return self.name
    
# Table alocacao
class Allocation(models.Model):
    start_date = models.DateField(
        'Start Date',
        null=False,
        blank=False,
    )
    leave_date = models.DateField(
        'Leave Date',
        null=True,
        blank=True,
    )
    id_departament = models.ForeignKey(
        Departament,
        related_name='allocation_departament',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name=('Departament')
    )
    id_employee = models.ForeignKey(
        Employee,
        related_name='employee_allocated',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    
    def __str__(self) -> str:
        return self.departament

# Table relacao_alocacao_funcao
class RelationAllocationRole(models.Model):
    allocation = models.ForeignKey(
        Allocation,
        related_name='allocation_related',
        on_delete=models.CASCADE,
        null=True,
    )
    id_role = models.ForeignKey(
        Role,
        related_name='role_related',
        on_delete=models.CASCADE,
        null=True,
    )
   
    def __str__(self) -> str:
        return f'{self.allocation} - {self.id_role}'
    
class Document(models.Model):
    id_employee = models.ForeignKey(
        Employee,
        related_name='employee_doc',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    file_name = models.CharField(
        db_column='tx_file_name',
        max_length=80,
        null=True,
        blank=True,
        verbose_name=('File Name')
    )
    
    def __str__(self) -> str:
        return self.file_name
    
class GenerateQrCode(models.Model):
    qr_code = models.CharField(
        'Code',
        max_length=80,
        null=False,
        blank=False,
    )
    
    def __str__(self) -> str:
        return self.code

class Register(models.Model):
    class TypeRegister(models.TextChoices):
        ENTRADA = 'E', ('Entrada')
        SAIDA = 'S', ('Saída')
     
    date_time_register = models.DateTimeField(
        'Date of clock Register',
        null=False,
        blank=False,
    )
    type_clock_register = models.CharField(
        'Type of Clock Register',
        max_length=1,
        null=False,
        blank=False,
        choices=TypeRegister.choices,
    )
    
    def __str__(self) -> str:
        return f'{self.date_time_register} for {self.type_clock_register}'

