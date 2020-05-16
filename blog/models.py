from django.db import models
from django.utils import timezone

# Create your models here.
class BlogPost (models.Model) :
    
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField()  
    tag = models.CharField(max_length=30, blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title

