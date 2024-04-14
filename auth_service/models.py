from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import user_logged_in, user_login_failed
from django.dispatch import receiver
from utils.utils import get_client_ip
from django.db.models.signals import post_save


class UserLogins(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_logins')
    no_logins = models.PositiveIntegerField(default=0)
    failed_attempts = models.PositiveIntegerField(default=0)
    # no_devices = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.user.username + '_logins'

    class Meta:
        verbose_name = 'User Login'
        verbose_name_plural = 'User Logins'
        db_table = 'UserLogins_DB'


class UserIP(models.Model):
    user_logins = models.ForeignKey(UserLogins, on_delete=models.CASCADE, related_name='ips')
    ip = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    failed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user_logins.user.username) + '_ip'

    class Meta:
        verbose_name = 'User IPs'
        verbose_name_plural = 'User IP'
        db_table = 'UserIP_DB'


class UserDevice(models.Model):
    user_logins = models.ForeignKey(UserLogins, on_delete=models.CASCADE, related_name='devices')
    device_name = models.CharField(max_length=100)
    is_phone = models.BooleanField(default=False)
    browser = models.CharField(max_length=100)
    os = models.CharField(max_length=100)

    @classmethod
    def get_user_device(cls, request, user):
        device_name = request.user_agent.device.family
        is_phone = request.user_agent.is_mobile
        browser = request.user_agent.browser.family
        os = request.user_agent.os.family
        return cls(device_name=device_name, is_phone=is_phone, browser=browser, os=os, user_logins=user.user_logins)

    def __str__(self):
        return str(self.user_logins.user.username) + '_device'

    class Meta:
        verbose_name = 'User Devices'
        verbose_name_plural = 'User Device'
        db_table = 'UserDevice_DB'


class UserProfile(models.Model):
    user_logins = models.ForeignKey(UserLogins, on_delete=models.CASCADE, related_name='user_profiles')
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=11, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='images/avatar', blank=True, null=True)
    clinic_name = models.CharField(max_length=100, blank=True, null=True)
    license = models.IntegerField(blank=True, null=True)

    MALE = 'male'
    FEMALE = 'female'
    GENDER = [(MALE, 'male'), (FEMALE, 'female')]
    gender = models.CharField(max_length=100, choices=GENDER, blank=True, null=True)

    def __str__(self):
        return str(self.user_logins.user.username) + '_profile'

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'Users Profiles'
        db_table = 'UserProfile_DB'


@receiver(signal=post_save, sender=User)
def create_user_logins(sender, instance, created, **kwargs):
    """create user_logins obj after user created"""
    if created:
        user_login = UserLogins(user=instance)
        user_login.save()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ create profile_user obj after user created """
    if created:
        profile = UserProfile(user_logins=instance.user_logins)
        profile.save()


# noinspection PyUnusedLocal becouse of fixed local ip
@receiver(signal=user_logged_in)
def add_user_ip(sender, request, user, **kwargs):
    """add user ip after user logged in"""
    ip = UserIP(user_logins=user.user_logins, ip=get_client_ip(request))
    user.user_logins.no_logins += 1
    user.user_logins.save()
    ip.save()


@receiver(signal=user_logged_in)
def add_user_device(sender, request, user, **kwargs):
    """add user device after user logged in"""
    device = UserDevice.get_user_device(request, user)
    device.save()


# todo: must be test it on product
@receiver(user_login_failed)
def login_failed(sender, credentials, request, user=None, **kwargs):
    # for product
    if user is not None:
        ip = UserIP(user_logins=user.user_logins, ip=get_client_ip(request), failed=True)
        user.user_logins.failed_attempts += 1
        user.user_logins.save()
        ip.save()
    else:
        # for admin panel
        try:
            user_login = UserLogins.objects.get(user__username=credentials.get('username'))
            user_login.user_logins += 1
            user_login.save()
            ip = UserIP(user_logins=user_login, ip=get_client_ip(request), failed=True)
            ip.save()
        except UserLogins.DoesNotExist:
            pass
