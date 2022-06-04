from rest_framework import serializers
from malaria import models


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hospital
        fields = ['id', 'name', 'email', 'phone', 'city',
                  'sub_city', 'woreda', 'isActive']


class RegisteredPersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RegisteredPersonnel
        fields = ['id', 'name', 'email', 'phone', 'city', 'sub_city', 'woreda',
                  'profile_picture', 'description', 'hospital_id', 'isActive']


class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Credential
        fields = ['id', 'role', 'email', 'password', ]


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = ['id', 'name', 'phone', 'city', 'sub_city', 'woreda',
                  'age', ]


class PatientCheckupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PatientCheckup
        fields = ['id', 'patient', 'fever', 'chills', 'headache', 'nausea', 'vomiting', 'diarrhea', 'abdominal_pain', 'muscle_pain', 'joint_pain',
                  'fatigue', 'rapid_breathing', 'rapid_heart_rate', 'cough',  'bmi', 'blood_pressure', 'temperature']


class RequestDiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RequestDiagnostic
        fields = ['id', 'patient_name', 'result', 'doctor_name',
                  'lab_technician_name', 'cell_image', ]


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prescription
        fields = ['id', 'patient_name', 'medicine_name', 'doctor_name',
                  'instruction', ]
