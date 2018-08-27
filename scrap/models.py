from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


class Technology(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Organization(models.Model):
    org_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    precis = models.CharField(max_length = 200)
    image_url = models.URLField(blank=True)
    description = models.TextField(max_length=900, default='')
    # technology_tags = ArrayField(models.CharField(max_length=200))
    technology_tags = models.ManyToManyField(Technology, blank = True)
    topic_tags = ArrayField(models.CharField(max_length=200))

    def __str__(self):
        return self.name

class Project(models.Model):
    organization = models.ForeignKey('scrap.Organization', on_delete=models.CASCADE)
    project_id = models.BigIntegerField()
    title = models.CharField(max_length = 200)
    display_name = models.CharField(max_length=200)
    description = models.TextField(max_length=900, default='')
    assignee_display_names = ArrayField(models.CharField(max_length=200))


    def __str__(self):
        return self.display_name
