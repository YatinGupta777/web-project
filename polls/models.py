from django.db import models
import datetime
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text

    #def was_published_recently(self):
    #    now = timezone.now()
    #    return now - datetime.timedelta(days=1)<=self.publish_date<=now
    #was_published_recently.admin_order_field = 'publish_date'#for admin side
    #was_published_recently.boolean = True#for admin side
    #was_published_recently.short_description = 'Published recently?'#for admin side

    def get_absolute_url(self):#THIS IS IMPORTANT && fucntion name cannot be changed
            return reverse('polls:index')

class Choice(models.Model):
    question_text = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def get_absolute_url(self):#THIS IS IMPORTANT && fucntion name cannot be changed
            return reverse('polls:index')
