# Generated by Django 3.1 on 2020-12-27 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_alias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alias',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aliases', to='players.player'),
        ),
    ]
