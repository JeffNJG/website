from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

# on recupere le model User par defaut (meilleure methode)
User = get_user_model()

class Participation(models.Model):
    """Modele d'association entre un user et un groupe"""
    
    join_date = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=255, null=True, blank=True, default="member")
    # comme c'est une classe d'association elle doit contenir des references
    # vers les classes associees
    childgroup = models.ForeignKey('ChildGroup', models.CASCADE)
    profile = models.ForeignKey('Profile', models.CASCADE)
    
    
class ChildGroup(models.Model):
    """Model to represent a child (local to a city) group"""
    
    url = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    school = models.CharField(max_length=255, null=True, blank=True)
    

class Profile(models.Model):
    """model which represent a user profile.
    All attributes are optional"""
    
    number = models.CharField(max_length=255, null=True, blank=True)
    whatsapp = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    skype = models.CharField(max_length=255, null=True, blank=True)
    github = models.CharField(max_length=255, null=True, blank=True)
    gitlab = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    sexe = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(User, models.CASCADE)
    group = models.ManyToManyField(ChildGroup, through=Participation)
    
    
class Project(models.Model):
    """Model to represent a project"""
    
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    link = models.CharField(max_length=255, null=True, blank=True)
    members = models.ManyToManyField(User)
    
    
class Article(models.Model):
    """Model to represent an article"""
    
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    posted_by = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    
    
class Event(models.Model):
    """Model to represent an event"""
    TYPES = [('Conference', 'Conference'), ('Meetup', 'Meetup'),
             ('Worksop', 'Workshop')]
    
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    location = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    posted_by = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    
    
class EventMedia(models.Model):
    """Modele to represent media of an event"""
    TYPES = [('Video', 'Video'), ('Image', 'Image')]
    
    type = models.CharField(max_length=255, null=True, blank=True, choices=TYPES)
    url = models.CharField(max_length=255, null=True, blank=True)
    miniature = models.CharField(max_length=255, null=True, blank=True)
    event = models.ForeignKey(Event, models.CASCADE)
