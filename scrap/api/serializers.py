from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from scrap.models import Organization, Technology, Topic, Project

# class TechnologySerializer(ModelSerializer):
#     class Meta:
#         model = Technology
#         fields = (
#             'name',
#         )

class ProjectsSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'organization',
            'project_id',
            'title',
            'display_name',
            'description',
            'assignee_display_names',
            'project_code_url',
        )

class OrganizationSerializer(ModelSerializer):
    # technology_tags = TechnologySerializer(many=True, read_only=True)
    technology_tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )
    topic_tags = serializers.SlugRelatedField(
        many=True,
        read_only = True,
        slug_field = 'name'
    )

    projects_data= ProjectsSerializer(source='get_all_projects', many=True)

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
            'projects_data',
        )
