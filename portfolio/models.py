from django.db import models
from django.utils.text import slugify


# Create your models here.

class skill_header(models.Model):
    header = models.CharField(max_length=50)
    
    def __str__(self):
        return self.header

class Skill(models.Model):  
  name = models.CharField(max_length=100)
  sheader = models.ForeignKey(skill_header, on_delete=models.CASCADE)

  def __str__(self):
      return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title



class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title