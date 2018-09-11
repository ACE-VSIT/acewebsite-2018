from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

from multiselectfield import MultiSelectField

from portalapp.models import ACEUserProfile
from website.models import Agenda


class Assignment(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=69)
    text = models.TextField()
    difficulty = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])

    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title


class Solution(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(ACEUserProfile, on_delete=models.CASCADE)
    submission = models.TextField()
    approval = models.BooleanField(default=False)

    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} - {1}'.format(self.submitted_by, self.assignment)


class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def count(self):
        resources = Resources.objects.filter(category=self.category)
        return len(resources)

    def __str__(self):
        return self.category

    class Meta:
        ordering = ['category']


class Resources(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    course = models.CharField(max_length=30)
    res_type = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    url = models.CharField(max_length=150)
    author = models.CharField(max_length=30)
    approval_status = models.BooleanField(default=False)
    difficulty = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    picture = models.CharField(max_length=100)

    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.course


try:
    members = ACEUserProfile.objects.filter(is_member=True)
    member_choices = list((x.name.id, x.name.first_name + ' ' + x.name.last_name) for x in members)
except:
    member_choices = []


class Attendance(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    member_choices = member_choices
    attended = MultiSelectField(choices=member_choices)

    def __str__(self):
        return self.agenda.name + " - (" + str(len(self.attended)) + " participated )"

