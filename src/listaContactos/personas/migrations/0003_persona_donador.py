# Generated by Django 5.0.6 on 2024-06-09 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_alter_persona_apellidos_alter_persona_edad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='donador',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
