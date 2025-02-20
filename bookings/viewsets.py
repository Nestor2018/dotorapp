from rest_framework import viewsets

from .serializers import AppointmentSerializer, MedicalNoteSerializer
from .models import Appointment, MedicalNote


class AppointmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows appointments to be viewed or edited.
    """

    queryset = Appointment.objects.all().order_by("date")
    serializer_class = AppointmentSerializer


class MedicalNoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows medical notes to be viewed or edited.
    """

    queryset = MedicalNote.objects.all().order_by("date")
    serializer_class = MedicalNoteSerializer
