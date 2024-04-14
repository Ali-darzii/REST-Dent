# Generated by Django 4.0 on 2024-04-14 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0012_procedure_user_logins'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dentalchart',
            old_name='tooth',
            new_name='adult_tooth',
        ),
        migrations.AddField(
            model_name='dentalchart',
            name='pediatric_tooth',
            field=models.JSONField(default=list),
        ),
    ]