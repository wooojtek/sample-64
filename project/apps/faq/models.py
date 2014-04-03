### Extend for models
from django.db import models
from autoslug import AutoSlugField
from django.core.urlresolvers import reverse


class QuestionType(models.Model):
    title = models.CharField(max_length=255, blank=False)
    slug = AutoSlugField(populate_from='title', max_length=255,
                         unique=True, always_update=True,
                         editable=True, blank=False)

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('faq.views.question_type', args=[self.slug])


class Question(models.Model):
    title = models.CharField(max_length=255, blank=False)
    slug = AutoSlugField(populate_from='title', max_length=255,
                         unique=True, always_update=True,
                         editable=True, blank=False)
    description = models.TextField(max_length=3001, blank=True)
    category = models.OneToOneField('QuestionType', related_name='questions', blank=False)

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('faq.views.question', args=[self.slug])