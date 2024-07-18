from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): # models.Model ensures django knowa this is a model to be used by the database
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #ForeignKey links to another model
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
