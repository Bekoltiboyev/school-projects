from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import Signal
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    tel_nomer = models.IntegerField(default=998)
    date_cleaned  = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='images/', default='default-avatar.png', null=True, blank=True)
    last_activity = models.DateTimeField(default=timezone.now)
    is_online = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.user)
    
class ProjectModel(models.Model):
    kurs = (
        ("frontend", "Frontend"),
        ("backend", "Backend"),
    )
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    date_cleaned  = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(upload_to='projectImage/')
    profiles = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    github_link = models.CharField(max_length=500, default='github-url')
    yonalish = models.CharField(max_length=20, default="Frontend", choices=kurs)
    
    
    def __str__(self) -> str:
        return self.name
    
class CommentModel(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, null=True)
    uptime = models.DateField(auto_now_add=True) 
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    user_profile_image = models.ImageField(upload_to='comment_user_images/', null=True, blank=True)
    
    def __str__(self):
        return self.name



def create_profile(sender, instance, created, **kwargs):  
    if created:
        Profile.objects.create(
            user=instance
        )
    else:
        profile = Profile.objects.get(user=instance)
        profile.email = instance.email
        profile.name = instance.first_name
        profile.save()
    
Signal.connect(post_save, create_profile, sender=User)

