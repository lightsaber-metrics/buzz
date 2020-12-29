# Generated by Django 3.1 on 2020-12-29 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20201220_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dynasty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Dynasties',
            },
        ),
        migrations.AddField(
            model_name='team',
            name='dynasty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='teams.dynasty'),
        ),
    ]
