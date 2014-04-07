from vanilla import CreateView

from .models import Contact


class CreateContact(CreateView):
    template_name = 'contact/email_form.jade'
    model = Contact
    success_url = '/'