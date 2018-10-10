from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.authtoken.models import Token
from scrap.models import Organization, Technology, Topic, Project
from rest_framework.serializers import (
    CharField,
)

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

class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = serializers.CharField()
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'token',
        ]
        extra_kwargs= {"password": {"write_only":True}}
    
    def validate(self, data):
        user_obj = None
        username = data.get('username', None)
        password = data.get('password', None)
        if not username:
            raise ValidationError("A username is required to login.")
        user = User.objects.filter(
            Q(username=username)
        ).distinct()
        if user.exists() and user.count()==1:
            user_obj = user.first()
        else:
            raise ValidationError("This username is not valid.")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials please try again.")
        token, _ = Token.objects.get_or_create(user=user_obj)
        data["token"] = token
        return data
