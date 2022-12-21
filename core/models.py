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
        max_length=80,
        null=True,
        blank=True,
        )

# Table cargo
class Post(ModelBase):
    name = models.CharField(
        max_length=80,
    )
    salary = models.FloatField(
        
    )
    scholarity = models.ForeignKey(
        'Scholarity',
        on_delete=models.CASCADE,
        null=True,
        )

# Table funcao
class Function(ModelBase):
    name = models.CharField(
        max_length=80,
    )
    description = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    scholarity = models.ForeignKey(
        'Scholarity',
        on_delete=models.CASCADE,
        null=True,
    )

# Table departamento
class Departament(ModelBase):
    name = models.CharField(
        max_length=80,
    )
    description = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )

# Table vinculo
class Bond(ModelBase):
    obs = models.CharField(
        max_length=200,
    )
    description = models.CharField(
        max_length=80,
        null=True,
        blank=True,
    )

# Table servidor
class Employee(ModelBase):
    name = models.CharField(
        max_length=80,
    )
    ra = models.CharField(
        max_length=15,
    )
    birth_date = models.DateField(

    )
    admission_date = models.DateField(

    )
    address = models.CharField(
        max_length=80,
    )
    district = models.CharField(
        max_length=80,
    )
    city = models.CharField(
        max_length=80,
    )
    post_code = models.CharField(
        max_length=15,
    )
    state = models.CharField(
        max_length=2,
    )
    phone = models.CharField(
        max_length=15,
    )
    email = models.EmailField(
        max_length=80,
    )
    password = models.CharField(
        max_length=15,
    )
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        null=True,
    )
    bond = models.ForeignKey(
        'Bond',
        on_delete=models.CASCADE,
        null=True,
    )

# Table alocacao
class Allocation(ModelBase):
    output_date = models.DateField(

    )
    start_data = models.DateField(

    )
    departament = models.ForeignKey(
        'Departament',
        on_delete=models.CASCADE,
        null=True,
    )
    employee = models.ForeignKey(
        'Employee',
        on_delete=models.CASCADE,
        null=True,
    )

# Table relacao_alocacao_funcao
class RelationAllocationFunction(ModelBase):
    allocation = models.ForeignKey(
        'Allocation',
        on_delete=models.CASCADE,
        null=True,
    )
    function = models.ForeignKey(
        'Function',
        on_delete=models.CASCADE,
        null=True,
    )
