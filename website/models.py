from django.db import models
from cloudinary.models import CloudinaryField

from portalapp.models import ACEUserProfile


class Image(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    picture = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return '{0}'.format(self.name)


class Project(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=150, null=True)
    developed = models.BooleanField(default=True)
    description = models.TextField(max_length=500, null=True)
    created_by = models.ManyToManyField(ACEUserProfile, null=True, blank=True)
    tools = models.CharField(max_length=100)
    picture = CloudinaryField('image', null=True, blank=True)
    source_code = models.URLField(null=True, blank=True)
    live_url = models.URLField(null=True, blank=True)
    when = models.DateField()

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
    description = models.TextField(max_length=500)
    event_type = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()

    images = models.ManyToManyField(Image)
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
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ManyToManyField(Image)

    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}'.format(self.name)


class Agenda(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    agenda_type = models.CharField(max_length=50)  # TODO[Sameer] - Add choices like 'ACEHOURS'
    start_date = models.DateField()
    end_date = models.DateField()
    time = models.TimeField(null=True, blank=True)

    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}'.format(self.name)


class Mentor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150, blank=True, null=True)
    about = models.TextField(max_length=500, blank=True, null=True)
    picture = CloudinaryField('image', null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    behance = models.URLField(null=True, blank=True)


    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}'.format(self.name)

class Alumni(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150)
    about = models.TextField(max_length=500, blank=True, null=True)
    acd_year = models.CharField(max_length=50)
    picture = CloudinaryField('image', null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    behance = models.URLField(null=True, blank=True)


    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}'.format(self.name)
