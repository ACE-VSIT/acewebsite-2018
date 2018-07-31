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
    enrollment_number = models.CharField(max_length=11,null =True,blank=True)
    dept = models.CharField(max_length=6,default='BCA')
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

class Projects(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=150,null=True)
    developed = models.BooleanField(default=True)
    desc = models.TextField(max_length=500,null=True)
    created_by = models.CharField(max_length=100)
    tools = models.CharField(max_length=100)
    photos = models.URLField(null=True, blank=True)
    url_code = models.URLField(null=True, blank=True)
    url_project = models.URLField(null=True, blank=True)
    class Meta:
        db_table = 'projects'
        verbose_name_plural = "Projects"

    def __str__(self):
        return '{0}'.format(self.id)

class Event(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=150)
    desc = models.TextField(max_length=500)
    ev_type = models.CharField(max_length =10)
    ev_date = models.DateField()

    event_head = models.CharField(max_length=100)
    photos = models.URLField(null=True, blank=True)
    registration_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return '{0}'.format(self.id)
    
class Achievements(models.Model):
    id = models.BigAutoField(primary_key=True)

    team = models.CharField(max_length=150)
    ev_name = models.CharField(max_length=500,blank=True)
    college_name = models.CharField(max_length =10)
    fest_name = models.CharField(max_length=100,blank=True)
    ev_date = models.DateField()
    
    photos = models.URLField(null=True, blank=True)

    def __str__(self):
        return '{0}'.format(self.id)

class Photo(models.Model):
    id = models.BigAutoField(primary_key=True)
    desc = models.TextField(max_length=500)
    imag = models.URLField(null=True, blank=True)

    def __str__(self):
        return '{0}'.format(self.id)
    

class UpEvent(models.Model):#needs changes
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=150)
    desc = models.TextField(max_length=500)
    ev_type = models.CharField(max_length =10)
    ev_date = models.DateField()
    event_head = models.CharField(max_length=100)
    poster = models.URLField(null=True, blank=True)
    registration_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return '{0}'.format(self.id)

class Calendar(models.Model):#needs changes
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=150)
    desc = models.TextField(max_length=500)
    ev_type = models.CharField(max_length =10)
    ev_date = models.DateField()
    event_head = models.CharField(max_length=100)

    def __str__(self):
        return '{0}'.format(self.id)

    

    



