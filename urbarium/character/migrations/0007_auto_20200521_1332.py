# Generated by Django 3.0.4 on 2020-05-21 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0006_auto_20200519_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='surname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
