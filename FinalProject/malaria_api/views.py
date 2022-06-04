from malaria import models
from malaria_api import serializers
from rest_framework import generics
import coreapi
from rest_framework.schemas import AutoSchema


class MalariaViewSchema(AutoSchema):

    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field('desc')
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class HospitalList(generics.ListCreateAPIView):
    schema = MalariaViewSchema()
    queryset = models.Hospital.objects.all()
    serializer_class = serializers.HospitalSerializer


class HospitalDetail(generics.RetrieveDestroyAPIView):
    schema = MalariaViewSchema()
    queryset = models.Hospital.objects.all()
    serializer_class = serializers.HospitalSerializer


class RegisteredPersonnelList(generics.ListCreateAPIView):
    schema = MalariaViewSchema()
    queryset = models.RegisteredPersonnel.objects.all()
    serializer_class = serializers.RegisteredPersonnelSerializer


class RegisteredPersonnelDetail(generics.RetrieveDestroyAPIView):
    schema = MalariaViewSchema()
    queryset = models.RegisteredPersonnel.objects.all()
    serializer_class = serializers.RegisteredPersonnelSerializer


class CredentialList(generics.ListCreateAPIView):
    schema = MalariaViewSchema()
    queryset = models.Credential.objects.all()
    serializer_class = serializers.CredentialSerializer


class CredentialDetail(generics.RetrieveDestroyAPIView):
    schema = MalariaViewSchema()
    queryset = models.Credential.objects.all()
    serializer_class = serializers.CredentialSerializer


class PatientList(generics.ListCreateAPIView):
    schema = MalariaViewSchema()
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer


class PatientDetail(generics.RetrieveDestroyAPIView):
    schema = MalariaViewSchema()
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer


class PatientCheckupList(generics.ListCreateAPIView):
    schema = MalariaViewSchema()
    queryset = models.PatientCheckup.objects.all()
    serializer_class = serializers.PatientCheckupSerializer


class PatientCheckupDetail(generics.RetrieveDestroyAPIView):
    schema = MalariaViewSchema()
    queryset = models.PatientCheckup.objects.all()
    serializer_class = serializers.PatientCheckupSerializer


class RequestDiagnosticList(generics.ListCreateAPIView):
    schema = MalariaViewSchema()
    queryset = models.RequestDiagnostic.objects.all()
    serializer_class = serializers.RequestDiagnosticSerializer


class RequestDiagnosticDetail(generics.RetrieveDestroyAPIView):
    schema = MalariaViewSchema()
    queryset = models.RequestDiagnostic.objects.all()
    serializer_class = serializers.RequestDiagnosticSerializer


class PrescriptionList(generics.ListCreateAPIView):
    schema = MalariaViewSchema()
    queryset = models.Prescription.objects.all()
    serializer_class = serializers.PrescriptionSerializer


class PrescriptionDetail(generics.RetrieveDestroyAPIView):
    schema = MalariaViewSchema()
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PrescriptionSerializer
