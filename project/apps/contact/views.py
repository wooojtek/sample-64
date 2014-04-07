# from django.conf import settings
# from django.core.mail import send_mail
from vanilla import CreateView

from .models import Contact


class CreateContact(CreateView):
    template_name = 'contact/email_form.jade'
    model = Contact
    success_url = '/'


    # success_url = '/email-sent/'
    #
    # def form_valid(self, form):
    #     message = "{name} / {email} said: ".format(
    #         name=form.cleaned_data.get('name'),
    #         email=form.cleaned_data.get('email'))
    #     message += "\n\n{0}".format(form.cleaned_data.get('message'))
    #     send_mail(
    #         subject=form.cleaned_data.get('subject').strip(),
    #         message=message,
    #         from_email="enquiries@xeontek.com",
    #         recipient_list=[settings.LIST_OF_EMAIL_RECIPIENTS],
    #     )
    #     return super(CreateContact, self).form_valid(form)