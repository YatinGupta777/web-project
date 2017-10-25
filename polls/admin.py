from django.contrib import admin
from polls.models import Question,Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('TITLEEEE HEREE',               {'fields': ['question_text']}),
        #('Date information', {'fields': ['publish_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','publish_date')#,'was_published_recently')
    list_filter = ['publish_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
