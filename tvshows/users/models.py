from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
User = get_user_model()

class TvShow(models.Model):
    name = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200)
    vote_average = models.FloatField()
    tv_id = models.FloatField(default=0)

class Suggestion(models.Model):
    show = models.OneToOneField(TvShow, on_delete=models.CASCADE)
    suggested_by = models.OneToOneField(User, on_delete=models.CASCADE)    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved_shows = models.ManyToManyField(TvShow, blank=True)
    suggested_shows = models.ManyToManyField(Suggestion, blank=True)
    
    def __str__(self):
        return self.user.username

def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)

post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)
