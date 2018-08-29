from django.core.management.base import BaseCommand

from scrap.gsocdata import organization_data, project_data
from scrap.models import Organization, Project, Technology, Topic

class Command(BaseCommand):
    help = 'Import all the org and Project data'

    def handle(self, *args, **options):
        organization_list = organization_data()
        for org in organization_list:
            technology_object_list = []
            topics_object_list = []
            for tag in org['technology_tags']:
                technology_object, created = Technology.objects.get_or_create(
                    name=tag.strip())
                technology_object_list.append(technology_object)
            for topic in org['topic_tags']:
                topic_object, created = Topic.objects.get_or_create(
                    name=topic.strip())
                topics_object_list.append(topic_object)
            org_object, created = Organization.objects.get_or_create(
                org_id=org['id'], name=org['name'], precis=org['precis'],
                image_url=org['image_url'],
                irc_channel= org['irc_channel'],
                mailing_list=org['mailing_list'], ideas_list=org['ideas_list'],
                blog_url=org['blog_url'], website_url=org['website_url'],
                description=org['description'])
            org_object.technology_tags.add(*technology_object_list)
            org_object.topic_tags.add(*topics_object_list)
            project_data(org['id'], org_object)
