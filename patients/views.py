from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .serializers import PatientSerializer
from .models import Patient


# GET  /api/patients => list_patients
# POST  /api/patients => create_patient


class ListPatientsView(ListCreateAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


# GET  /api/patients/pk => Detalle
# PUT  /api/patients/pk => Modificación
# DELETE  /api/patients/pk => Borrar


class DetailPatientView(RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
