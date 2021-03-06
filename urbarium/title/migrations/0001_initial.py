# Generated by Django 3.0.4 on 2020-05-18 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('character', '0003_auto_20200513_1832'),
        ('governing_body', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('concerning', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='governing_body.GoverningBody')),
                ('holders', models.ManyToManyField(to='character.Character')),
            ],
        ),
    ]
