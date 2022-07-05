# Generated by Django 4.0.5 on 2022-06-28 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre del Doctor')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido del Doctor')),
                ('profesion', models.CharField(max_length=30, verbose_name='Profesión del Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre del Paciente')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido del Paciente')),
                ('edad', models.PositiveIntegerField(verbose_name='Edad del Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Posgrados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre del Posgrado')),
                ('comision', models.IntegerField(verbose_name='Comisión')),
            ],
        ),
    ]