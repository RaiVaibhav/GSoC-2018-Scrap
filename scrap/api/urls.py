from django.urls import path, include, re_path
from .views import OrganizationListAPIView, ProjectListAPIView, UserLoginView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken import views

app_name = 'scrap'
urlpatterns = [
    re_path(r'login', UserLoginView.as_view(), name='api_login'),
    # re_path(r'sampleapi', sample_api),
    re_path(r'organizations', OrganizationListAPIView.as_view(), name='orglist'),
    re_path(r'projects', ProjectListAPIView.as_view(), name='projectlist'),
]
