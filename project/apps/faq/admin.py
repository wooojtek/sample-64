from django.contrib import admin

from .models import QuestionType, Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category', 'description']
    readonly_fields = ['title', 'slug', 'category', 'description']
    list_filter = ['category']


admin.site.register(QuestionType)
admin.site.register(Question, QuestionAdmin)