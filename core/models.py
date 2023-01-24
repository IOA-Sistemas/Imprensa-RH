from django.db import models
from django.contrib.auth import get_user_model
Employees = get_user_model()
# import random
# from account.models import User

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
    
    class Meta: 
        db_table = 'tb_roles'

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
    
    class Meta: 
        db_table = 'tb_departaments'

# Table vinculo
class EmploymentAssociation(models.Model):
    class Type(models.TextChoices):
        CLT = 'C', ('CLT')
        PJ = 'P', ('PJ')
        OUTSOURCED = 'O', ('Tercerizado')
        TRAINEE = 'E', ('Estágio')
    
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
    
    class Meta: 
        db_table = 'tb_employment_associations'


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
        Employees,
        related_name='employee_allocated',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    
    def __str__(self) -> str:
        return self.departament
    
    class Meta: 
        db_table = 'employees_allocations'

# Table relacao entre alocacao e funcoes
class AllocationRoles(models.Model):
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
    
    class Meta: 
        db_table = 'tb_allocation-roles'
    
class Document(models.Model):
    id_employee = models.ForeignKey(
        Employees,
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
    
    class Meta: 
        db_table = 'tb_document'
    
class GenerateQrCode(models.Model):
    qr_code = models.CharField(
        'Code',
        max_length=80,
        null=False,
        blank=False,
    )
    
    def __str__(self) -> str:
        return self.code
    
    class Meta: 
        db_table = 'tb_qrcode'

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
    
    class Meta: 
        db_table = 'tb_registers'

