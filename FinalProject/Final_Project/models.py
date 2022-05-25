import email
from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, default=" ")
    city = models.CharField(max_length=100)
    sub_city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    woreda = models.CharField(max_length=10)
    isActive = models.BooleanField(default=True)


class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    sub_city = models.CharField(max_length=100)
    woreda = models.CharField(max_length=10)
    profile_picture = models.CharField(max_length=300, default=" ")
    description = models.TextField(max_length=500, default=" ")
    hospital_id = models.IntegerField()
    isActive = models.BooleanField(default=True)


class Credential(models.Model):
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)


class RequestDiagnostic(models.Model):
    patient_name = models.CharField(max_length=200)
    result = models.CharField(max_length=100, default="Pending")
    doctor_name = models.CharField(max_length=200)
    lab_technician_name = models.CharField(max_length=200)
    cell_image = models.CharField(max_length=300)


class Patient(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    age = models.IntegerField
    sub_city = models.CharField(max_length=100)
    woreda = models.CharField(max_length=10)
    symptoms = models.TextField(max_length=500)
    bmi = models.FloatField(max_length=5)
    temperature = models.FloatField(max_length=5)
    blood_pressure = models.FloatField(max_length=5)
    heart_beat = models.FloatField(max_length=5)


class Prescription(models.Model):
    patient_name = models.CharField(max_length=200)
    medicine_name = models.CharField(max_length=200)
    doctor_name = models.CharField(max_length=200)
    instruction = models.CharField(max_length=200)
