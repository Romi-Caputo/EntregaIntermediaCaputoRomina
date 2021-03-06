# Generated by Django 4.0.5 on 2022-07-11 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0005_doctor_especialidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='apellido',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='especialidad',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='apellido',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='edad',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='residencia',
            name='comision',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='residencia',
            name='especialidad',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='residencia',
            name='horario',
            field=models.IntegerField(),
        ),
    ]
