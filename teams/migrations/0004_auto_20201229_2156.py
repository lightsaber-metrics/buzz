# Generated by Django 3.1 on 2020-12-29 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20201229_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='dynasty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teams', to='teams.dynasty'),
        ),
    ]
