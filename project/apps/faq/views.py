__author__ = 'wb'

from django.shortcuts import render, get_object_or_404

from .models import QuestionType, Question


def faq_index(request):
    return render(request, 'faq/faq_index.jade', {
        'question_types': QuestionType.objects.all(),
        'questions': Question.objects.all()
    })


def question(request, slug):
    # get the Post object
    question = get_object_or_404(Question, slug=slug)
    # now return the rendered template
    return render(request, 'faq/question.jade', {'question': question})


def question_type(request, slug):
    question_type = get_object_or_404(QuestionType, slug=slug)
    return render(request, 'faq/question_type.jade', {
        'question_type': question_type,
        'question': Question.objects.filter(question_type=question_type)
    })

