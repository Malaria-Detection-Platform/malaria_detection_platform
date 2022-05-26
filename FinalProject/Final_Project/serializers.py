from rest_framework import serializers
from Final_Project import models


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hospital
        fields = ['name','email', 'phone', 'city',
                  'sub_city', 'woreda', 'isActive']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ['id', 'name', 'email', 'phone', 'city', 'sub_city', 'woreda',
                  'profile_picture', 'description', 'hospital_id', 'isActive']


class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Credential
        fields = ['id', 'role', 'email', 'password', ]


class RequestDiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RequestDiagnostic
        fields = ['id', 'patient_name', 'result', 'doctor_name',
                  'lab_technician_name', 'cell_image', ]


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = ['id', 'name', 'email', 'phone', 'city', 'sub_city', 'woreda',
                  'age', 'symptoms', 'bmi', 'blood_pressure', 'temperature']


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prescription
        fields = ['id', 'patient_name', 'medicine_name', 'doctor_name',
                  'instruction', ]
