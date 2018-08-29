from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from markdown_deux import markdown
from django.utils.safestring import mark_safe

class Technology(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Organization(models.Model):
    org_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    precis = models.CharField(max_length = 200)
    image_url = models.URLField(blank=True)
    irc_channel = models.URLField(null=True)
    mailing_list = models.URLField(null=True)
    ideas_list = models.URLField(blank=True)
    blog_url= models.URLField(null=True)
    website_url = models.URLField(blank=True)
    description = models.TextField(max_length=900, default='')
    technology_tags = models.ManyToManyField(Technology, blank = True)
    topic_tags = models.ManyToManyField(Topic, blank = True)

    def __str__(self):
        return self.name

    def get_markdown(self):
        description = self.description
        return mark_safe(markdown(description))

    def get_orgsite(self):
        return ('https://summerofcode.withgoogle.com/organizations/'+str(self.org_id))


class Project(models.Model):
    organization = models.ForeignKey('scrap.Organization', on_delete=models.CASCADE)
    project_id = models.BigIntegerField()
    title = models.CharField(max_length = 200)
    display_name = models.CharField(max_length=200)
    description = models.TextField(max_length=900, default='')
    assignee_display_names = ArrayField(models.CharField(max_length=200))
    project_code_url = models.URLField(blank=True)


    def __str__(self):
        return self.display_name
