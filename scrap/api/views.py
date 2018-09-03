from rest_framework.generics import ListAPIView

from scrap.models import Organization, Technology, Project
from .serializers import OrganizationSerializer

class OrganizationListAPIView(ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
