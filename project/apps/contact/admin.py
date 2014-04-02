__author__ = 'wb'

from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['subject', 'email']
    search_fields = ['subject', 'email', 'content']
    list_filter = ['subject', 'email']


admin.site.register(Contact, ContactAdmin)

