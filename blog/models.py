from django.db import models

# Create your models here.
class BlogPost (models.Model) :
    
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField()

    def __unicode__(self):
        return self.title

