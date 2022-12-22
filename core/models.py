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

# Table escolaridade
class Scholarity(ModelBase):
    description = models.CharField(
        db_column='description',
        max_length=80,
        null=True,
        blank=True,
    )

# Table cargo
class Post(ModelBase):
    name = models.CharField(
        db_column='name',
        max_length=80,
        null=False,
        blank=False,
    )
    salary = models.FloatField(
        db_column='salary',
        null=False,
        blank=False,
    )
    scholarity = models.ForeignKey(
        'Scholarity',
        db_column='scholarity',
        on_delete=models.CASCADE,
        null=True,
    )

# Table funcao
class Function(ModelBase):
    name = models.CharField(
        db_column='name',
        max_length=80,
        null=False,
        blank=False,
    )
    description = models.CharField(
        db_column='description',
        max_length=200,
        null=True,
        blank=True,
    )
    scholarity = models.ForeignKey(
        'Scholarity',
        db_column='scholarity',
        on_delete=models.CASCADE,
        null=True,
    )

# Table departamento
class Departament(ModelBase):
    name = models.CharField(
        db_column='name',
        max_length=80,
        null=False,
        blank=False,
    )
    description = models.CharField(
        db_column='description',
        max_length=200,
        null=True,
        blank=True,
    )

# Table vinculo
class Bond(ModelBase):
    obs = models.CharField(
        db_column='obs',
        max_length=200,
        null=False,
        blank=False,
    )
    description = models.CharField(
        db_column='description',
        max_length=80,
        null=True,
        blank=True,
    )

# Table servidor
class Employee(ModelBase):
    name = models.CharField(
        db_column='name',
        max_length=80,
        null=False,
        blank=False,
    )
    ra = models.CharField(
        db_column='ra',
        max_length=15,
        null=False,
        blank=False,
    )
    birth_date = models.DateField(
        db_column='birth_date',
        null=False,
        blank=False,
    )
    admission_date = models.DateField(
        db_column='admission_date',
        null=False,
        blank=False,
    )
    address = models.CharField(
        db_column='address',
        max_length=80,
        null=False,
        blank=False,
    )
    district = models.CharField(
        db_column='district',
        max_length=80,
        null=False,
        blank=False,
    )
    city = models.CharField(
        db_column='city',
        max_length=80,
        null=False,
        blank=False,
    )
    post_code = models.CharField(
        db_column='post_code',
        max_length=15,
        null=False,
        blank=False,
    )
    state = models.CharField(
        db_column='state',
        max_length=2,
        null=False,
        blank=False,
    )
    phone = models.CharField(
        db_column='phone',
        max_length=15,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        db_column='email',
        max_length=80,
        null=False,
        blank=False,
    )
    password = models.CharField(
        db_column='password',
        max_length=15,
        null=False,
        blank=False,
    )
    post = models.ForeignKey(
        'Post',
        db_column='post',
        on_delete=models.CASCADE,
        null=True,
    )
    bond = models.ForeignKey(
        'Bond',
        db_column='bond',
        on_delete=models.CASCADE,
        null=True,
    )

# Table alocacao
class Allocation(ModelBase):
    output_date = models.DateField(
        db_column='output_date',
        null=False,
        blank=False,
    )
    start_data = models.DateField(
        db_column='start_data',
        null=False,
        blank=False,
    )
    departament = models.ForeignKey(
        'Departament',
        db_column='departament',
        on_delete=models.CASCADE,
        null=True,
    )
    employee = models.ForeignKey(
        'Employee',
        db_column='employee',        
        on_delete=models.CASCADE,
        null=True,
    )

# Table relacao_alocacao_funcao
class RelationAllocationFunction(ModelBase):
    allocation = models.ForeignKey(
        'Allocation',
        db_column='allocation',
        on_delete=models.CASCADE,
        null=True,
    )
    function = models.ForeignKey(
        'Function',
        db_column='function',
        on_delete=models.CASCADE,
        null=True,
    )
