from django.db import models

# Create your models here.

'''
class Events(models.Model):
    id = models.BigAutoField(primary_key=True)

    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'events'
        verbose_name_plural = "Events"

    def __str__(self):
        return '{0}'.format(self.id)
'''

class Members(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=100, null=True, blank=True)
    core = models.BooleanField(default=False) # required?
    position = models.CharField(max_length=30, default='Member')

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
        verbose_name_plural = "Members"

    def __str__(self):
        return '{0}'.format(self.id)

