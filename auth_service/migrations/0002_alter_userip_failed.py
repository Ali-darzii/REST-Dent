# Generated by Django 4.2 on 2024-02-12 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userip',
            name='failed',
            field=models.BooleanField(default=False),
        ),
    ]