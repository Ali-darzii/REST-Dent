from django.db import models

# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'
    GENDER = [(MALE, 'male'), (FEMALE, 'female'), (OTHER, 'other')]
    gender = models.CharField(max_length=100, choices=GENDER)

    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    job = models.CharField(max_length=200, blank=True, null=True)
    emergency_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
        db_table = 'Patient_DB'