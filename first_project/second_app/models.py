from django.db import models

# Create your models here.

class CyberStories(models.Model):
    Title = models.CharField(max_length=264)
    Link = models.CharField(max_length=264)
    Published = models.DateField()
    Description = models.CharField(max_length=100)

    def __str__(self):
        return self.Title
