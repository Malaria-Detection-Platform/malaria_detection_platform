from django.http import JsonResponse
from Final_Project import models
from Final_Project import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def hospital_list(request):
    if request.method == 'GET':
        hospitals = models.Hospital.objects.all()
        serializer = serializers.HospitalSerializer(hospitals, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.HospitalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def hospital_detail(request, id):
    try:
        hospital = models.Hospital.objects.get(pk=id)
    except models.Hospital.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.HospitalSerializer(hospital)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.HospitalSerializer(
            hospital, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        hospital.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def person_list(request):
    if request.method == 'GET':
        people = models.Person.objects.all()
        serializer = serializers.PersonSerializer(people, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = serializers.PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def person_detail(request, id):
    try:
        person = models.Person.objects.get(pk=id)
    except models.Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.PersonSerializer(person)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def credential_list(request):
    if request.method == 'GET':
        credentials = models.Credential.objects.all()
        serializer = serializers.CredentialSerializer(credentials, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = serializers.CredentialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def credential_detail(request, id):
    try:
        credential = models.Credential.objects.get(pk=id)
    except models.Credential.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.CredentialSerializer(credential)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.CredentialSerializer(
            credential, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        credential.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def request_diagnostic_list(request):
    if request.method == 'GET':
        request_diagnostics = models.RequestDiagnostic.objects.all()
        serializer = serializers.RequestDiagnosticSerializer(
            request_diagnostics, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = serializers.RequestDiagnosticSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def request_diagnostic_detail(request, id):
    try:
        request_diagnostic = models.RequestDiagnostic.objects.get(pk=id)
    except models.RequestDiagnostic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.RequestDiagnosticSerializer(
            request_diagnostic)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.RequestDiagnosticSerializer(
            request_diagnostic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        request_diagnostic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def patient_list(request):
    if request.method == 'GET':
        patients = models.Patient.objects.all()
        serializer = serializers.PatientSerializer(patients, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = serializers.PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def patient_detail(request, id):
    try:
        patient = models.Patient.objects.get(pk=id)
    except models.Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.PatientSerializer(
            patient)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.PatientSerializer(
            patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def prescription_list(request):
    if request.method == 'GET':
        prescriptions = models.Prescriptions.objects.all()
        serializer = serializers.PrescriptionSerializer(
            prescriptions, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = serializers.PrescriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def prescription_detail(request, id):
    try:
        prescription = models.Prescription.objects.get(pk=id)
    except models.Prescription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.PrescriptionSerializer(
            prescription)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.PrescriptionSerializer(
            prescription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        prescription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
