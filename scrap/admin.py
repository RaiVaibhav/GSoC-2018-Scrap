from django.contrib import admin
from .models import Organization, Project, Technology

admin.site.register(Organization)
admin.site.register(Project)
admin.site.register(Technology)
