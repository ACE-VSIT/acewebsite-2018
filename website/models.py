from django.db import models
<<<<<<< HEAD
from s3direct.fields import S3DirectField
from portalapp.models import  ACEUserProfile
=======
from cloudinary.models import CloudinaryField
>>>>>>> 5afb6369ff7003b5066a482ebf32f15cea4bb829

from portalapp.models import ACEUserProfile

<<<<<<< HEAD
=======

class Image(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    picture = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return '{0}'.format(self.name)
>>>>>>> 5afb6369ff7003b5066a482ebf32f15cea4bb829


class Project(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=150, null=True)
    developed = models.BooleanField(default=True)
<<<<<<< HEAD
    desc = models.TextField(max_length=500, null=True)
    created_by = models.ManyToManyField( ACEUserProfile, null=True, blank=True)
=======
    description = models.TextField(max_length=500, null=True)
    created_by = models.ManyToManyField(ACEUserProfile, null=True, blank=True)
>>>>>>> 5afb6369ff7003b5066a482ebf32f15cea4bb829
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

<<<<<<< HEAD
    poc = models.ManyToManyField( ACEUserProfile, null=True, blank=True)
    #point of contact
    photos = S3DirectField(dest='events')
=======
    images = models.ManyToManyField(Image)
>>>>>>> 5afb6369ff7003b5066a482ebf32f15cea4bb829
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
