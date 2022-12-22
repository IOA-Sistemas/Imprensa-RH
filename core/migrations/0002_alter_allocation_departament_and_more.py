# Generated by Django 4.1.4 on 2022-12-22 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocation',
            name='departament',
            field=models.ForeignKey(db_column='departament', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.departament'),
        ),
        migrations.AlterField(
            model_name='allocation',
            name='employee',
            field=models.ForeignKey(db_column='employee', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.employee'),
        ),
        migrations.AlterField(
            model_name='allocation',
            name='output_date',
            field=models.DateField(db_column='output_date'),
        ),
        migrations.AlterField(
            model_name='allocation',
            name='start_data',
            field=models.DateField(db_column='start_data'),
        ),
        migrations.AlterField(
            model_name='bond',
            name='description',
            field=models.CharField(blank=True, db_column='description', max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='bond',
            name='obs',
            field=models.CharField(db_column='obs', max_length=200),
        ),
        migrations.AlterField(
            model_name='departament',
            name='description',
            field=models.CharField(blank=True, db_column='description', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='departament',
            name='name',
            field=models.CharField(db_column='name', max_length=80),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(db_column='address', max_length=80),
        ),
        migrations.AlterField(
            model_name='employee',
            name='admission_date',
            field=models.DateField(db_column='admission_date'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='birth_date',
            field=models.DateField(db_column='birth_date'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='bond',
            field=models.ForeignKey(db_column='bond', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.bond'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='city',
            field=models.CharField(db_column='city', max_length=80),
        ),
        migrations.AlterField(
            model_name='employee',
            name='district',
            field=models.CharField(db_column='district', max_length=80),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(db_column='email', max_length=80),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(db_column='name', max_length=80),
        ),
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(db_column='password', max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(db_column='phone', max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='post',
            field=models.ForeignKey(db_column='post', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.post'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='post_code',
            field=models.CharField(db_column='post_code', max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='ra',
            field=models.CharField(db_column='ra', max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='state',
            field=models.CharField(db_column='state', max_length=2),
        ),
        migrations.AlterField(
            model_name='function',
            name='description',
            field=models.CharField(blank=True, db_column='description', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='function',
            name='name',
            field=models.CharField(db_column='name', max_length=80),
        ),
        migrations.AlterField(
            model_name='function',
            name='scholarity',
            field=models.ForeignKey(db_column='scholarity', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.scholarity'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(db_column='name', max_length=80),
        ),
        migrations.AlterField(
            model_name='post',
            name='salary',
            field=models.FloatField(db_column='salary'),
        ),
        migrations.AlterField(
            model_name='post',
            name='scholarity',
            field=models.ForeignKey(db_column='scholarity', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.scholarity'),
        ),
        migrations.AlterField(
            model_name='relationallocationfunction',
            name='allocation',
            field=models.ForeignKey(db_column='allocation', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.allocation'),
        ),
        migrations.AlterField(
            model_name='relationallocationfunction',
            name='function',
            field=models.ForeignKey(db_column='function', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.function'),
        ),
        migrations.AlterField(
            model_name='scholarity',
            name='description',
            field=models.CharField(blank=True, db_column='description', max_length=80, null=True),
        ),
    ]