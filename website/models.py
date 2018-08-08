from django.db import models
from s3direct.fields import S3DirectField


class Member(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=100, null=True, blank=True)
    enrollment_number = models.CharField(max_length=11, null=True, blank=True)
    image = S3DirectField(dest='members')
    dept = models.CharField(max_length=6, default='BCA')
    core = models.BooleanField(default=False)
    position = models.CharField(max_length=30)

    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    behance = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'members'
        verbose_name_plural = 'Members'

    def __str__(self):
        return '{0}'.format(self.name)


class Project(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=150, null=True)
    developed = models.BooleanField(default=True)
    desc = models.TextField(max_length=500, null=True)
    created_by = models.ManyToManyField(Member, null=True, blank=True)
    tools = models.CharField(max_length=100)
    screenshot = S3DirectField(dest='projects', null=True, blank=True)
    source_code = models.URLField(null=True, blank=True)
    live_url = models.URLField(null=True, blank=True)

    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'projects'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return '{0}'.format(self.name)


class Event(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=150)
    desc = models.TextField(max_length=500)
    event_type = models.CharField(max_length=10)
    event_date = models.DateField()

    poc = models.ManyToManyField(Member, null=True, blank=True)
    photos = S3DirectField(dest='events')
    registration_url = models.URLField(null=True, blank=True)

    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}'.format(self.name)


class Achievement(models.Model):
    id = models.BigAutoField(primary_key=True)

    team = models.CharField(max_length=150)
    event_name = models.CharField(max_length=500, blank=True)
    position = models.CharField(max_length=5)
    college_name = models.CharField(max_length=10)
    fest_name = models.CharField(max_length=100, blank=True)
    event_month = models.CharField(max_length=20)

    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}'.format(self.team)


class Gallery(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    desc = models.TextField(max_length=500)
    image = S3DirectField(dest='gallery') # models.URLField(null=True, blank=True)

    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}'.format(self.name)


class Calendar(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=150)
    desc = models.TextField(max_length=500)
    event_type = models.CharField(max_length=10)
    event_month = models.CharField(max_length=15)

    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}'.format(self.name)
