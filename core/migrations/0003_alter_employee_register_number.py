# Generated by Django 4.1.4 on 2023-01-18 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_employee_register_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='register_number',
            field=models.CharField(default=33274, max_length=5, verbose_name='Register Number'),
        ),
    ]