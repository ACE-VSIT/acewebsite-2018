from __future__ import unicode_literals
from django.db import models


class ACEUserProfile(models.Model):
    name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    enroll_number = models.CharField(max_length=11, blank=False, null=False)
    course = models.CharField(max_length=30, default=None, null=True, blank=True)
    email_id = models.EmailField()
    phone_number = models.CharField(max_length=10)  # validators should be a list
    is_member = models.BooleanField(default=False)
    is_core = models.BooleanField(default=False)
    section = models.CharField(max_length=3, blank=True, null=True)

    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    behance = models.URLField(null=True, blank=True)

    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.username


class Tasks(models.Model):
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
