from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import PatientSerializer
from .models import Patient


# GET  /api/patients => list_patients
# POST  /api/patients => create_patient


@api_view(["GET", "POST"])
def list_patients(request):
    if request.method == "GET":
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


# GET  /api/patients/pk => Detalle
# PUT  /api/patients/pk => Modificación


@api_view(["GET", "PUT"])
def detail_patient(request, pk):
    try:
        patient = Patient.objects.get(id=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = PatientSerializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
