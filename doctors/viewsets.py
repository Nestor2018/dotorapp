from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import (
    DoctorSerializer,
    DepartmentSerializer,
    DoctorAvailabilitySerializer,
    MedicalNoteSerializer,
)
from .models import Doctor, Department, DoctorAvailability, MedicalNote
from .permissions import IsDoctor


class DoctorViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite a los doctores ser vistos o editados.
    """

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly, IsDoctor]

    @action(["POST"], detail=True, url_path="set-on-vacation")
    def set_on_vacation(self, requests, pk):
        """
        Cambia el estado de los doctores a en vacaciones.
        """
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response({"is_on_vacation": doctor.is_on_vacation})

    @action(["POST"], detail=True, url_path="set-off-vacation")
    def set_off_vacation(self, requests, pk):
        """
        Cambia el estado de los doctores a que no esta en vacaciones.
        """
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({"is_on_vacation": doctor.is_on_vacation})


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite a los departamentos ser vistos o editados.
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite a las disponibilidades de los doctores ser vistos o editados.
    """

    queryset = DoctorAvailability.objects.all()
    serializer_class = DoctorAvailabilitySerializer


class MedicalNoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite a las notas médicas ser vistas o editadas.
    """

    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer
