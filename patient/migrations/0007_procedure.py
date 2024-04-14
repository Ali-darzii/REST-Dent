# Generated by Django 4.0 on 2024-04-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_rename_user_patient_user_logins'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('amount', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Procedure',
                'verbose_name_plural': 'Procedures',
                'db_table': 'Procedure_DB',
            },
        ),
    ]