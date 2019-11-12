from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=150, unique_for_date='publish')
    body = models.TextField()
    publish = models.dateTimeField(defoult=timezone.now)

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title
