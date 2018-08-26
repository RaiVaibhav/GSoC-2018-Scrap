# Generated by Django 2.1 on 2018-08-26 15:30

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('org_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('precis', models.CharField(max_length=200)),
                ('image_url', models.URLField(blank=True)),
                ('description', models.TextField(default='', max_length=900)),
                ('technology_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('topic_tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.BigIntegerField()),
                ('title', models.CharField(max_length=200)),
                ('display_name', models.CharField(max_length=200)),
                ('description', models.TextField(default='', max_length=900)),
                ('assignee_display_names', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrap.Organization')),
            ],
        ),
    ]
