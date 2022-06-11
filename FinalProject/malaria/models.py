from django.db import models
from authentication.models import User


# Create your models here.


class Hospital(models.Model):
    user = models.OneToOneField(
        User, related_name="hosptals", on_delete=models.CASCADE, default=None, null=True)
    name = models.CharField(max_length=200, default=" ")
    email = models.EmailField(max_length=100, default=" ")
    city = models.CharField(max_length=100, default=" ")
    sub_city = models.CharField(max_length=100, default=" ")
    phone = models.CharField(max_length=20, default=" ")
    woreda = models.CharField(max_length=10, default=" ")
    isActive = models.BooleanField(default=True)


class RegisteredPersonnel(models.Model):
    user = models.OneToOneField(
        User, related_name="personnel", on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200, default=" ")
    email = models.EmailField(max_length=200, default=" ")
    phone = models.CharField(max_length=20, default=" ")
    city = models.CharField(max_length=100, default=" ")
    sub_city = models.CharField(max_length=100, default=" ")
    woreda = models.CharField(max_length=10, default=" ")
    profile_picture = models.ImageField(max_length=300, default=" ")
    description = models.TextField(max_length=500, default=" ")
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)


class Patient(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    age = models.IntegerField
    sub_city = models.CharField(max_length=100)
    woreda = models.CharField(max_length=10)


class PatientCheckup(models.Model):
    patient = models.OneToOneField(
        Patient, related_name="patient", on_delete=models.CASCADE, default=None)
    bmi = models.FloatField(max_length=5)
    temperature = models.FloatField(max_length=5)
    blood_pressure = models.FloatField(max_length=5)
    heart_beat = models.FloatField(max_length=5)
    fever = models.BooleanField(default=False)
    chills = models.BooleanField(default=False)
    headache = models.BooleanField(default=False)
    nausea = models.BooleanField(default=False)
    vomiting = models.BooleanField(default=False)
    diarrhea = models.BooleanField(default=False)
    abdominal_pain = models.BooleanField(default=False)
    muscle_pain = models.BooleanField(default=False)
    joint_pain = models.BooleanField(default=False)
    rapid_breathing = models.BooleanField(default=False)
    fatigue = models.BooleanField(default=False)
    rapid_heart_rate = models.BooleanField(default=False)
    cough = models.BooleanField(default=False)


class RequestDiagnostic(models.Model):

    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE)
    result = models.CharField(max_length=100, default="Pending")
    doctor = models.ForeignKey(
        RegisteredPersonnel, on_delete=models.CASCADE, related_name="Doctor")
    lab_technician = models.ForeignKey(
        RegisteredPersonnel, on_delete=models.CASCADE, related_name="Lab_Technician")


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=200)
    doctor = models.ForeignKey(
        RegisteredPersonnel, on_delete=models.CASCADE)
    instruction = models.CharField(max_length=200)
