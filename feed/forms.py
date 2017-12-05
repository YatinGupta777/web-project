from django import forms
from feed.models import Post
<<<<<<< HEAD

=======
>>>>>>> f10ea429a7d7cdc1bb79e79af7c7061dce5e451a
from django.utils import timezone

class PostForm(forms.ModelForm):

    event_name = forms.CharField(required=True)
    event_image = forms.ImageField(required=False)
    event_date= forms.DateField(required=False,widget = forms.SelectDateWidget(years=range(2017, 2019)))
    event_time = forms.TimeField(required=False)
    event_society = forms.CharField(required=False)
    event_venue = forms.CharField(required=False)
    event_description = forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'editable medium-editor-textarea'}))

    class Meta():
        model = Post
        fields = ('event_name','event_image','event_date','event_time','event_society','event_society','event_venue','event_description')#Fields that can be edited

        #widgets = {
        #    'event_description':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        #}
