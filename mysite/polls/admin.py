from django.contrib import admin
from .models import Question, Choice

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'ques_text']
    fieldsets=[
        ('Question Description', {'fields':['ques_text']}),
        ('Date Information', {'fields': ['pub_date']})
    ]
    list_display = ('ques_text', 'pub_date')
    list_filter=['pub_date']
    search_fields=['ques_text']

    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)
admin.site.register(Choice)