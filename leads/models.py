from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Lead(models.Model):

    # SOURCE_CHOICES = (
    #     ('youtube', 'YouTube'),
    #     ('google', 'Google'),
    #     ('newsletter', 'NewsLetter')
    # )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=50)

    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)
