from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)
    
class Post(models.Model):
    categoty_list  = [('sunny','SUNNY'),('cloudy','CLOUDY'),('rainy','RAINY'),('windy','WINDY')]
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    weather = models.CharField(max_length=10, choices=categoty_list, default='-')
    tags = models.ManyToManyField(Tag)
    
    
    