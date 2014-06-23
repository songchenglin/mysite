from django.contrib import admin
from polls.models import Question
from polls.models import Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question', {'fields':['question_text']}),
        ('Date information', {'fields':['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    inlines = [ChoiceInline]
admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
