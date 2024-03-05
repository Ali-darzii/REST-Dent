# Generated by Django 4.2 on 2024-02-09 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_logins', models.PositiveIntegerField(default=0)),
                ('failed_attempts', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_logins', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Login',
                'verbose_name_plural': 'User Logins',
                'db_table': 'UserLogins_DB',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.CharField(blank=True, max_length=11, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/avatar')),
                ('clinic_name', models.CharField(blank=True, max_length=100, null=True)),
                ('license', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=100, null=True)),
                ('user_logins', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profiles', to='auth_service.userlogins')),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'Users Profiles',
                'db_table': 'UserProfile_DB',
            },
        ),
        migrations.CreateModel(
            name='UserIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('failed', models.BooleanField(default=True)),
                ('user_logins', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ips', to='auth_service.userlogins')),
            ],
            options={
                'verbose_name': 'User IPs',
                'verbose_name_plural': 'User IP',
                'db_table': 'UserIP_DB',
            },
        ),
        migrations.CreateModel(
            name='UserDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=100)),
                ('is_phone', models.BooleanField(default=False)),
                ('browser', models.CharField(max_length=100)),
                ('os', models.CharField(max_length=100)),
                ('user_logins', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='auth_service.userlogins')),
            ],
            options={
                'verbose_name': 'User Devices',
                'verbose_name_plural': 'User Device',
                'db_table': 'UserDevice_DB',
            },
        ),
    ]
