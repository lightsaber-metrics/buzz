# Generated by Django 3.1 on 2020-12-20 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_auto_20201216_0711'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='teams', to='players.Player'),
        ),
    ]
