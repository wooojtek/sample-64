from django.contrib import admin

from .models import QuestionType, Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category', 'description']
    list_filter = ['category']
    # actions = None
    # actions_on_top = False
    # actions_on_bottom = False
    # actions_selection_counter = False
    # list_display_links = []
    # list_editable = []


admin.site.register(QuestionType)
admin.site.register(Question, QuestionAdmin)