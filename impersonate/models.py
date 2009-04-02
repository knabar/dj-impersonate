from django.db import models
from django.contrib.auth.models import User, Group

class Impersonation(models.Model):
    user = models.ForeignKey(User, related_name='impersonating_set')
    users = models.ManyToManyField(User, related_name='impersonated_set', blank=True)
    groups = models.ManyToManyField(Group, related_name='impersonated_set', blank=True)
