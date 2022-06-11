from malaria import models
from malaria_api import serializers
from rest_framework import generics, permissions
import coreapi
from rest_framework.schemas import AutoSchema
from authentication import custom_permissions


class MalariaViewSchema(AutoSchema):

    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field('desc')
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class HospitalList(generics.ListAPIView):
    schema = MalariaViewSchema()
    permission_classes = [
        permissions.IsAuthenticated & custom_permissions.isAdmin]
    queryset = models.Hospital.objects.all()
    serializer_class = serializers.HospitalSerializer


class HospitalDetail(generics.RetrieveUpdateDestroyAPIView):
    schema = MalariaViewSchema()
    permission_classes = [
        permissions.IsAuthenticated & custom_permissions.isAdmin]
    queryset = models.Hospital.objects.all()
    serializer_class = serializers.HospitalSerializer


class RegisteredPersonnelList(generics.ListAPIView):
    schema = MalariaViewSchema()
    serializer_class = serializers.RegisteredPersonnelSerializer

    def get_queryset(self):
        queryset = models.RegisteredPersonnel.objects.all()
        user_id = self.request.query_params.get('id')
        queryset = queryset.filter(hospital__user_id=user_id)
        return queryset

    permission_classes = [permissions.IsAuthenticated &
                          custom_permissions.isEmployee]


class RegisteredPersonnelDetail(generics.RetrieveUpdateAPIView):
    schema = MalariaViewSchema()
    queryset = models.RegisteredPersonnel.objects.all()
    serializer_class = serializers.RegisteredPersonnelSerializer
    permission_classes = [permissions.IsAuthenticated &
                          custom_permissions.isEmployee & custom_permissions.hasWritePermission]


class ReceptionistPatientList(generics.ListCreateAPIView):
    schema = MalariaViewSchema()
    permission_classes = [permissions.IsAuthenticated &
                          custom_permissions.isReceptionist & custom_permissions.isOwnerPersonnel]

    def get_queryset(self):
        queryset = models.Patient.objects.all()
        hospital = self.request.query_params.get('hospital')
        queryset = queryset.filter(hospital=hospital)
        return queryset
    serializer_class = serializers.PatientSerializer


class ReceptionistPatientDetail(generics.RetrieveUpdateDestroyAPIView):
    schema = MalariaViewSchema()

    permission_classes = [permissions.IsAuthenticated &
                          custom_permissions.isReceptionist & custom_permissions.isOwnerPersonnel]

    def get_queryset(self):
        queryset = models.Patient.objects.all()
        hospital = self.request.query_params.get('hospital')
        queryset = queryset.filter(hospital=hospital)
        return queryset

    serializer_class = serializers.PatientSerializer


class DoctorPatientList(generics.ListAPIView):
    schema = MalariaViewSchema()

    permission_classes = [permissions.IsAuthenticated &
                          custom_permissions.isDoctor & custom_permissions.isDoctorOfPatient & custom_permissions.isOwnerPersonnel]

    def get_queryset(self):
        queryset = models.Patient.objects.all()
        user_id = self.request.query_params.get('id')
        queryset = queryset.filter(doctor__user_id=user_id)
        return queryset
    serializer_class = serializers.PatientSerializer


class DoctorPatientDetail(generics.RetrieveUpdateAPIView):
    schema = MalariaViewSchema()

    permission_classes = [permissions.IsAuthenticated &
                          custom_permissions.isDoctor & custom_permissions.isDoctorOfPatient & custom_permissions.isOwnerPersonnel]

    def get_queryset(self):
        queryset = models.Patient.objects.all()
        user_id = self.request.query_params.get('id')
        queryset = queryset.filter(doctor__user_id=user_id)
        return queryset
    serializer_class = serializers.PatientSerializer


class PatientCheckupList(generics.RetrieveUpdateAPIView):
    schema = MalariaViewSchema()
    permission_classes = [permissions.IsAuthenticated &
                          custom_permissions.isDoctor & custom_permissions.hasChecupListAccess]
    queryset = models.PatientCheckup.objects.all()
    serializer_class = serializers.PatientCheckupSerializer


class RequestDiagnosticList(generics.ListCreateAPIView):
    schema = MalariaViewSchema()
    permission_classes = [permissions.IsAuthenticated &
                          custom_permissions.isDoctor]

    def get_queryset(self):
        queryset = models.RequestDiagnostic.objects.all()
        user_id = self.request.query_params.get('id')
        queryset = queryset.filter(doctor__user_id=user_id)
        return queryset
    serializer_class = serializers.RequestDiagnosticSerializer


class RequestDiagnosticDetail(generics.RetrieveUpdateDestroyAPIView):
    schema = MalariaViewSchema()
    permission_classes = [permissions.IsAuthenticated &
                          custom_permissions.isDoctor]

    def get_queryset(self):
        queryset = models.RequestDiagnostic.objects.all()
        user_id = self.request.query_params.get('id')
        queryset = queryset.filter(doctor__user_id=user_id)
        return queryset
    serializer_class = serializers.RequestDiagnosticSerializer


class DiagnosticResult(generics.RetrieveUpdateAPIView):
    schema = MalariaViewSchema()
    permission_classes = [permissions.IsAuthenticated &
                          custom_permissions.isLabTech]

    def get_queryset(self):
        queryset = models.RequestDiagnostic.objects.all()
        user_id = self.request.query_params.get('id')
        queryset = queryset.filter(lab_technician__user_id=user_id)
        return queryset
    serializer_class = serializers.RequestDiagnosticSerializer


class PrescriptionList(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated &
                          custom_permissions.isDoctor]
    schema = MalariaViewSchema()

    def get_queryset(self):
        queryset = models.RequestDiagnostic.objects.all()
        user_id = self.request.query_params.get('id')
        queryset = queryset.filter(doctor__user_id=user_id)
        return queryset
    serializer_class = serializers.PrescriptionSerializer


class PrescriptionDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated &
                          custom_permissions.isDoctor & custom_permissions.isPrescriptionOfDoctor]
    schema = MalariaViewSchema()

    def get_queryset(self):
        queryset = models.RequestDiagnostic.objects.all()
        user_id = self.request.query_params.get('id')
        queryset = queryset.filter(doctor__user_id=user_id)
        return queryset
    serializer_class = serializers.PrescriptionSerializer
