from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    event_name = models.CharField(max_length=150,blank=False,null=True)
    event_image = models.ImageField(upload_to='media/feed/static/images')
    event_date = models.DateField(auto_now=False,blank=True,null=True)
    event_time = models.TimeField(auto_now=False,blank=True,null=True)
    event_society = models.CharField(max_length=100,blank=True,null=True)
    event_venue = models.CharField(max_length=100,blank=True,null=True)
    event_description = models.CharField(max_length=1500,blank=True,null=True)
    published_date = models.DateTimeField(blank=True,null=True,auto_now_add=True)

    def publish(self):#time is when publish button clicked
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):#THIS IS IMPORTANT && fucntion name cannot be changed
        return reverse("feed:post_detail",kwargs={'pk':self.pk})
