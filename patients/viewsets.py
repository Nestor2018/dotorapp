from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models import Patient, Insurance, MedicalRecord


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    @action(detail=True, methods=["get"], url_path="medical-records")
    def get_medical_records(self, request, pk):
        patient = self.get_object()
        return Response(patient.medical_history)


class InsuranceViewSet(viewsets.ModelViewSet):
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()


class MedicalRecordViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()
