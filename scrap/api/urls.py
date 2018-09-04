from django.urls import path, include, re_path
from .views import OrganizationListAPIView

app_name = 'scrap'
urlpatterns = [
    re_path(r'organizations/', OrganizationListAPIView.as_view(), name='orglist'),
]
