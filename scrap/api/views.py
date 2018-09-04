from rest_framework.generics import ListAPIView, RetrieveAPIView

from scrap.models import Organization, Technology, Project
from .serializers import OrganizationSerializer

class OrganizationListAPIView(ListAPIView):

    serializer_class = OrganizationSerializer
    def get_queryset(self):
        queryset = Organization.objects.all()
        org_id = self.request.query_params.get('org_id',None)
        if org_id is not None:
            queryset = Organization.objects.filter(pk=int(org_id))
        return queryset

# class OrganizationRetrieveAPIView(RetrieveAPIView):
#     serializer_class = OrganizationSerializer
#     # queryset = Organization.objects.get(pk=self.kwargs['pk'])
#     def get_queryset(self):
#         return Organization.objects.filter(pk=int(self.kwargs['pk']))
