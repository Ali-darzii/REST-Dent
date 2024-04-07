from django.db import models
from auth_service.models import UserLogins


# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'
    GENDER = [(MALE, 'male'), (FEMALE, 'female'), (OTHER, 'other')]
    gender = models.CharField(max_length=100, choices=GENDER)

    avatar = models.ImageField(upload_to='images/patients', blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    job = models.CharField(max_length=200, blank=True, null=True)
    emergency_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact = models.CharField(max_length=11, blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    user_logins = models.ForeignKey(UserLogins, on_delete=models.CASCADE, related_name='user_patient')

    def __str__(self):
        return f"{self.first_name} {self.last_name} => {self.user}"

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
        db_table = 'Patient_DB'
        ordering = ('-time_stamp',)
