__author__ = 'wb'

from django.contrib import admin

from .models import QuestionType, Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['QuestionType']


admin.site.register(QuestionType)
admin.site.register(Question, QuestionAdmin)
