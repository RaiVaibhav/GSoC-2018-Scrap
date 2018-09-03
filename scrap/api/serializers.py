from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from scrap.models import Organization, Technology, Topic

class TechnologySerializer(ModelSerializer):
    class Meta:
        model = Technology
        fields = (
            'name',
        )

class OrganizationSerializer(ModelSerializer):
    technology_tags = TechnologySerializer(many=True, read_only=True)
    class Meta:
        model = Organization
        fields = (
            'org_id',
            'name',
            'precis',
            'image_url',
            'irc_channel',
            'mailing_list',
            'ideas_list',
            'blog_url',
            'website_url',
            'description',
            'technology_tags',
            'topic_tags',
        )
