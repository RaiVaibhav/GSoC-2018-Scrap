from django.urls import path, include, re_path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    re_path(r'^$', views.tag_display, name='tag_list'),
    # re_path(r'^orglist/$', views.list_display, name='list_display'),
]
