# Generated by Django 5.0.4 on 2024-04-16 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0002_interest'),
    ]

    operations = [
        migrations.AddField(
            model_name='interest',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
