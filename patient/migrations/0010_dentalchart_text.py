# Generated by Django 4.0 on 2024-04-07 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0009_dentalchart_procedure_alter_dentalchart_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='dentalchart',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]