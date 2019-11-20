from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug' : self.slug})


    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title
