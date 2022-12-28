from django.db import models
# Create your models here.
class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        primary_key=True,
    )
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name= 'Created at'
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified',
        auto_now=True,
        null=True,
        blank=True,
        verbose_name= 'Modified at'
    )
    is_active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True,
        verbose_name= 'Active'
    )

    class Meta:
        abstract = True

# Table cargo
class Role(ModelBase):
    class Scholarity(models.TextChoices):
        MEDIO_INCOMPLETO = 'MI', ('Ensino Médio Incompleto')
        MEDIO_COMPLETO = 'MC', ('Ensino Médio Completo')
        SUPERIOR_INCOMPLETO = 'SI', ('Superior Incompleto')
        SUPERIOR_COMPLETO = 'SC', ('Superior Completo')
        MESTRADO = 'M', ('Mestrado'),
        DOUTORADO = 'D', ('Doutorado')
    
    role_name = models.CharField(
        db_column='tx_role_name',
        max_length=80,
        null=False,
        blank=False,
        verbose_name=('Role Name')
    )
    salary = models.FloatField(
        db_column='nb_salary',
        null=False,
        blank=False,
        verbose_name=('Salary')
    )
    scholarity = models.CharField(
        db_column='cs_scholarity',
        max_length=2,
        null=False,
        blank=False,
        choices=Scholarity.choices,
        verbose_name=('Scholarity')
    )
    graduation = models.CharField(
        db_column='tx_graduation',
        null=True,
        blank=True,
        max_length=80,
        verbose_name=('Graduation')
    )
    role_description = models.TextField(
        db_column='tx_role_desc',
        null=False,
        blank=False,
        verbose_name=('Role Description')
    )

# Table departamento
class Departament(ModelBase):
    departament_name = models.CharField(
        db_column='tx_departament_name',
        max_length=80,
        null=False,
        blank=False,
        verbose_name=('Departament Name')
    )
    description = models.CharField(
        db_column='description',
        max_length=200,
        null=True,
        blank=True,
        verbose_name=('Departament Description')
    )

# Table vinculo
class EmploymentBond(ModelBase):
    class Type(models.TextChoices):
        CLT = 'C', ('CLT')
        PJ = 'P', ('PJ')
        TRAINEE = 'T', ('Trainee')
    
    type = models.CharField(
        db_column='cs_type',
        max_length=200,
        null=False,
        blank=False,
        choices=Type.choices,
        verbose_name=('Type of Employment Bond')
    )
    description = models.CharField(
        db_column='tx_description',
        max_length=80,
        null=True,
        blank=True,
        verbose_name=('Description')
    )

# Table servidor
class Employee(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=80,
        null=False,
        blank=False,
        verbose_name=('Name')
    )
    register_number = models.CharField(
        db_column='tx_register_number',
        max_length=5,
        null=False,
        blank=False,
        verbose_name=('Register Number')
    )
    birth_date = models.DateField(
        db_column='dt_birth_date',
        null=False,
        blank=False,
        verbose_name=('BirthDate')
    )
    admission_date = models.DateField(
        db_column='dt_admission_date',
        null=False,
        blank=False,
        verbose_name=('Admission Date')
    )
    address = models.CharField(
        db_column='tx_address',
        max_length=80,
        null=False,
        blank=False,
        verbose_name=('Adress')
    )
    neighborhood = models.CharField(
        db_column='tx_neighborhood',
        max_length=80,
        null=False,
        blank=False,
        verbose_name=('Neighborhood')
    )
    city = models.CharField(
        db_column='tx_city',
        max_length=80,
        null=False,
        blank=False,
        verbose_name=('City')
    )
    post_code = models.CharField(
        db_column='tx_post_code',
        max_length=15,
        null=False,
        blank=False,
        verbose_name=('Post Code')
    )
    state = models.CharField(
        db_column='tx_state',
        max_length=2,
        null=False,
        blank=False,
        verbose_name=('State')
    )
    phone = models.IntegerField(
        db_column='nb_phone',
        null=False,
        blank=False,
        verbose_name=('Phone')
    )
    email = models.EmailField(
        db_column='tx_email',
        max_length=80,
        null=False,
        blank=False,
        verbose_name=('Email')
    )
    role = models.ForeignKey(
        'Role',
        db_column='id_role',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name=('Role')
    )
    bond = models.ForeignKey(
        'EmploymentBond',
        db_column='id_bond',
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        verbose_name=('Employee Bond')
    )

# Table alocacao
class Allocation(ModelBase):
    start_date = models.DateField(
        db_column='dt_start_date',
        null=False,
        blank=False,
        verbose_name=('Start Date')
    )
    leave_date = models.DateField(
        db_column='dt_leave_date',
        null=True,
        blank=True,
        verbose_name=('Leave Date')
    )
    departament = models.ForeignKey(
        'Departament',
        db_column='id_departament',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name=('Departament')
    )
    employee = models.ForeignKey(
        'Employee',
        db_column='id_employee',        
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name=('Employee')
    )

# Table relacao_alocacao_funcao
class RelationAllocationFunction(ModelBase):
    allocation = models.ForeignKey(
        'Allocation',
        db_column='id_allocation',
        on_delete=models.CASCADE,
        null=True,
        verbose_name=('Allocation')
    )
    role = models.ForeignKey(
        'Role',
        db_column='id_role',
        on_delete=models.CASCADE,
        null=True,
        verbose_name=('Role')
    )
    
class Document(ModelBase):
    employee = models.ForeignKey(
        'Employee',
        db_column='id_employee',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=('Employee')
    )
    file_name = models.CharField(
        db_column='tx_file_name',
        max_length=80,
        null=True,
        blank=True,
        verbose_name=('File Name')
    )
    
class Code(ModelBase):
    code = models.CharField(
        db_column='tx_code',
        max_length=80,
        null=False,
        blank=False,
        verbose_name=('Code')
    )

class Register(ModelBase):
    class TypeRegister(models.TextChoices):
        ENTRADA = 'E', ('Entrada')
        SAIDA = 'S', ('Saída')
     
    date_clock_register = models.DateField(
        db_column='dt_clock_register',
        null=False,
        blank=False,
        verbose_name=('Date of clock Register')
    )
    hour_clock_register = models.TimeField(
        db_column='tm_clock_register',
        null=False,
        blank=False,
        verbose_name=('Time of clock Register')
    )
    type_clock_register = models.CharField(
        db_column='cs_type_clock_register',
        max_length=1,
        null=False,
        blank=False,
        choices=TypeRegister.choices,
        verbose_name=('Type of Clock Register')
    )


