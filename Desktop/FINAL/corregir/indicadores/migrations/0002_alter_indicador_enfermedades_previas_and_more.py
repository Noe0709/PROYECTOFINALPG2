# Generated by Django 5.1.2 on 2024-10-08 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicador',
            name='enfermedades_previas',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='indicador',
            name='familiar_enfermedad',
            field=models.CharField(max_length=90),
        ),
    ]