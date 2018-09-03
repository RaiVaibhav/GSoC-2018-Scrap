from django.urls import path, include, re_path
from .views import OrganizationListAPIView

app_name = 'scrap'
urlpatterns = [
    # re_path(r'^$', views.tag_display, name='tag_list'),
    # re_path(r'^orglist/$', views.list_display, name='list_display'),
    re_path(r'^$', OrganizationListAPIView.as_view(), name='orglist')
]
