from django.contrib import admin
from .models import Organization, Project, Technology, Topic

admin.site.register(Organization)
admin.site.register(Project)
admin.site.register(Technology)
admin.site.register(Topic)
