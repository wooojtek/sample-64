from django.core.urlresolvers import reverse_lazy
from vanilla import CreateView, DeleteView, ListView, UpdateView

from .models import Question


class ListQuestion(ListView):
    template_name = 'faq/question_list.jade'
    model = Question


class CreateQuestion(CreateView):
    template_name = 'faq/question_form.jade'
    model = Question
    success_url = reverse_lazy('list_question')


class EditQuestion(UpdateView):
    template_name = 'faq/question_form.jade'
    model = Question
    success_url = reverse_lazy('list_question')


class DeleteQuestion(DeleteView):
    model = Question
    success_url = reverse_lazy('list_question')