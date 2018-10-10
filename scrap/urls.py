from django.urls import path, include, re_path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    re_path(r'^$', views.tag_display, name='tag_list'),
    # re_path(r'^orglist/$', views.list_display, name='list_display'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^login/$',  LoginView.as_view(template_name='scrap/login.html'), name="login"),
    re_path(r'^logout/$', views.logout_session, name='logout'),
]
