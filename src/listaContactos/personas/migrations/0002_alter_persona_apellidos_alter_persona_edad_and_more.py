# Generated by Django 5.0.6 on 2024-06-09 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='apellidos',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='edad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombres',
            field=models.CharField(max_length=100),
        ),
    ]
