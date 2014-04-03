from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail

from .forms import ContactForm


def contact(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = ContactForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            form.save()
            message = "{name} / {email} said: ".format(
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'))
            message += "\n\n{0}".format(form.cleaned_data.get('message'))
            send_mail(
                subject=form.cleaned_data.get('subject').strip(),
                message=message,
                from_email="enquiries@xeontek.com",
                recipient_list=[settings.LIST_OF_EMAIL_RECIPIENTS]
            )
            return redirect('/email-sent/')  # Redirect after POST
    else:
        form = ContactForm()  # An unbound form
    return render(request, 'contact/email_form.jade', {
        'form': form,
    })





    # from django.conf import settings
    # from django.core.mail import send_mail
    # from django.views.generic import FormView
    # from .forms import ContactForm
    #
    #
    # class ContactFormView(FormView):
    #     form_class = ContactForm
    #     template_name = "contact/email_form.jade"
    #     success_url = '/email-sent/'
    #
    #     def form_valid(self, form):
    #         message = "{name} / {email} said: ".format(
    #             name=form.cleaned_data.get('name'),
    #             email=form.cleaned_data.get('email'))
    #         message += "\n\n{0}".format(form.cleaned_data.get('message'))
    #         send_mail(
    #             subject=form.cleaned_data.get('subject').strip(),
    #             message=message,
    #             from_email="enquiries@xeontek.com",
    #             recipient_list=[settings.LIST_OF_EMAIL_RECIPIENTS],
    #         )
    #         return super(ContactFormView, self).form_valid(form)