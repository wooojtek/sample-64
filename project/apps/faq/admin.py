from django.contrib import admin

from .models import QuestionType, Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'description', 'category']
    list_filter = ['category']


admin.site.register(QuestionType)
admin.site.register(Question, QuestionAdmin)
