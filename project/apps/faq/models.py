from django.db import models
from autoslug import AutoSlugField
from taggit.managers import TaggableManager


class QuestionType(models.Model):
    title = models.CharField(max_length=255, blank=False)
    slug = AutoSlugField(populate_from='title', max_length=255,
                         unique=True, always_update=True, blank=False)

    def __unicode__(self):
        return u'%s' % self.title


class Question(models.Model):
    title = models.CharField(max_length=255, blank=False)
    slug = AutoSlugField(populate_from='title', max_length=255,
                         unique=True, always_update=True, blank=False)
    description = models.TextField(max_length=3001, blank=True)
    category = models.OneToOneField('QuestionType', related_name='questions', blank=False)
    tags = TaggableManager()

    # def get_absolute_url(self):
    #     return reverse('faq.views.question', args=[self.slug])