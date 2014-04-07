from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['subject', 'name', 'email', 'phone', 'message']
    readonly_fields = ['subject', 'name', 'email', 'phone', 'message']
    list_filter = ['subject']

admin.site.register(Contact, ContactAdmin)