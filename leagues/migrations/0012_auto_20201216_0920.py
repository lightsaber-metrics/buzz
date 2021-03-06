# Generated by Django 3.1 on 2020-12-16 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0011_auto_20201216_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bracket',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brackets', to='leagues.season'),
        ),
    ]
