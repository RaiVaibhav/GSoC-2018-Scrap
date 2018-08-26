from django.core.management.base import BaseCommand

from scrap.gsocdata import organization_data, project_data
from scrap.models import Organization, Project

class Command(BaseCommand):
    help = 'Import all the org and Project data'

    def handle(self, *args, **options):
        organization_list = organization_data()
        # import pdb; pdb.set_trace()
        for org in organization_list:
            # import pdb; pdb.set_trace()
            org_object, created = Organization.objects.get_or_create(
                org_id=org['id'], name=org['name'], precis=org['precis'],
                image_url=org['image_url'], description=org['description'],
                technology_tags=org['technology_tags'],
                topic_tags=org['topic_tags'])
            project_data(org['id'], org_object)
