### Extend for models
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=14, blank=True, help_text='Optional')
    inquiry = (
        ('question', 'I have a question'),
        ('helpdesk', 'Help/Support'),
        ('callback', 'Please give me a call')
    )
    subject = models.CharField(max_length=8, choices=inquiry)
    message = models.TextField()

    def __unicode__(self):
        return u'%s' % self.subject