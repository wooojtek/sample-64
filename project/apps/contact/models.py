### Extend for models

from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(help_text='Enter your email address i.e. email@example.com')
    phone = models.CharField(max_length=14, blank=True)  # as optional
    inquiry = (
        ('question', 'I have a question'),
        ('helpdesk', 'Help/Support'),
        ('callback', 'Please give me a call')
    )
    subject = models.CharField(max_length=8, choices=inquiry)
    message = models.TextField()
    # created = models.DateTimeField(auto_now_add=True)
    #
    # class Meta:
    #     ordering = ['-created']

    def __unicode__(self):
        return u'%s' % self.subject


        # from crispy_forms.helper import FormHelper
        # from crispy_forms.layout import Submit
        # import floppyforms as forms
        #
        #
        # class ContactForm(forms.Form):
        #     name = forms.CharField(required=True)
        #     email = forms.EmailField(required=True)
        #     subject = forms.CharField(required=True)
        #     message = forms.CharField(widget=forms.Textarea)
        #
        #     def __init__(self, *args, **kwargs):
        #         self.helper = FormHelper()
        #         self.helper.add_input(Submit('submit', 'Submit'))
        #         super(ContactForm, self).__init__(*args, **kwargs)