# Generated by Django 3.1 on 2021-01-10 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0006_auto_20201220_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='awardcategory',
            name='discord_emoji',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
