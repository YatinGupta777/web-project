from django import forms
from polls.models import Question,Choice

class ChoiceForm(forms.ModelForm):

    class Meta():
        model = Choice
        fields = ('question_text','choice_text')#Fields that can be edited

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Needed to initialize fields dictionary
        self.fields['question_text'].required = True
        self.fields['choice_text'].required = True
    #    widgets = {
    #        'question_text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
    #        'choice_text':  forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
    #    }
