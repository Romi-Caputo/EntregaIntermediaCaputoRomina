# Generated by Django 4.0.5 on 2022-07-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0002_rename_doctores_doctor_rename_pacientes_paciente_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Residencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(max_length=30, verbose_name='Nombre de la Especialidad')),
                ('comision', models.IntegerField(verbose_name='Comisión')),
                ('horario', models.IntegerField(verbose_name='Horario')),
            ],
        ),
        migrations.DeleteModel(
            name='Posgrado',
        ),
    ]
