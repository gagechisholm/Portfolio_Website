from django.db import models

# Create your models here.
# portfolio/models.py
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField()  # 1-100%

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)
    github_link = models.URLField(blank=True)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
