from django.core.management.base import BaseCommand

from scrap.gsocdata import organization_data, project_data
from scrap.models import Organization, Project, Technology

class Command(BaseCommand):
    help = 'Import all the org and Project data'

    def handle(self, *args, **options):
        organization_list = organization_data()
        for org in organization_list:
            technology_object_list = []
            for tag in org['technology_tags']:
                technology_object, created = Technology.objects.get_or_create(
                    name=tag)
                technology_object_list.append(technology_object)

            org_object, created = Organization.objects.get_or_create(
                org_id=org['id'], name=org['name'], precis=org['precis'],
                image_url=org['image_url'], description=org['description'],
                topic_tags=org['topic_tags'])
            org_object.technology_tags.add(*technology_object_list)
            project_data(org['id'], org_object)
