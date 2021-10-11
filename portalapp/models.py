from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class ACEUserProfile(models.Model):
    
    """
    This model is used to store profiles of users.
    """
    
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    enroll_number = models.CharField(max_length=11, blank=False, null=False)
    course = models.CharField(max_length=30, default=None, null=True, blank=True)
    email_id = models.EmailField()
    phone_number = models.CharField(max_length=10)  # validators should be a list
    section = models.CharField(max_length=3, blank=True, null=True)

    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    behance = models.URLField(null=True, blank=True)

    is_member = models.BooleanField(default=False)
    is_core = models.BooleanField(default=False)
    is_council = models.BooleanField(default=False)
    position = models.TextField(null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)
    picture = CloudinaryField('image', null=True, blank=True)

    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def get_membership(self):
        if self.is_core:
            return 'Core Member'
        elif self.is_member:
            return 'Member'
        else:
            return ''

    def __str__(self):
        return '{0} {1}'.format(self.name.first_name, self.name.last_name)


class Tasks(models.Model):
    
    """
    This model is used to store list of available tasks.
    """
    
    task_id = models.CharField(max_length=20, primary_key=True)
    task_name = models.CharField(max_length=30)
    submission_deadline = models.CharField(max_length=10)
    difficulty_level = models.CharField(max_length=50)
    difficulty_value = models.CharField(max_length=30, default='Easy')
    task_description = models.TextField()
    total_submissions = models.IntegerField(default=0)

    def __str__(self):
        return '{0} ({1})'.format(self.task_name, self.difficulty_value)


class Submissions(models.Model):
    
    """
    This model is used to store submissions of users for particular tasks.
    """
    
    class Meta:
        unique_together = (('user', 'task'),)

    user = models.ForeignKey(ACEUserProfile, on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    task_submitted = models.BooleanField(default=False)
    submission_url = models.TextField(blank=True)

    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task.task_name
