# Generated by Django 4.2.16 on 2024-09-22 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_fish_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='image_url',
            field=models.CharField(blank=True, default='images/default-fish.png', max_length=255, null=True),
        ),
    ]
