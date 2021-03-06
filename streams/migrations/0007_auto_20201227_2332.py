# Generated by Django 3.1 on 2020-12-27 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_auto_20201227_1928'),
        ('streams', '0006_auto_20201227_0531'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='players.player'),
        ),
        migrations.AlterField(
            model_name='stream',
            name='service',
            field=models.CharField(choices=[('TW', 'Twitch'), ('YT', 'Youtube')], default='TW', max_length=2),
        ),
    ]
