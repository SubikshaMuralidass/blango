#from django.db import models

# Create your models here.
"""from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Image(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=200, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Image for {self.event.name}"
"""

#from djongo import models
from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(blank=True)
    #slug = models.SlugField(unique=True default='', blank=True)
    slug = models.SlugField(unique=True, default='', blank=True)  # New field added


    #objects = models.DjongoManager()
    objects = models.Manager()

    def __str__(self):
        return self.name

"""class Image(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=200, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    #objects = models.DjongoManager()
    objects = models.Manager()

    def __str__(self):
        return f"Image for {self.event.name}"
"""