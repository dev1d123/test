# Generated by Django 5.0.6 on 2024-05-30 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.TextField()),
                ('apellidos', models.TextField()),
                ('edad', models.TextField()),
            ],
        ),
    ]
