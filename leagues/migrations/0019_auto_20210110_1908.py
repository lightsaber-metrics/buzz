# Generated by Django 3.1 on 2021-01-10 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0018_auto_20210110_1908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='round',
            options={'ordering': ['bracket', 'round_number', '-name']},
        ),
        migrations.RenameField(
            model_name='round',
            old_name='round_number_new',
            new_name='round_number',
        ),
    ]
