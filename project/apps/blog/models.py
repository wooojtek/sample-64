from django.core.urlresolvers import reverse
from django.db import models
from autoslug import AutoSlugField
from taggit.managers import TaggableManager


class Category(models.Model):
    title = models.CharField(max_length=255, blank=False)
    slug = AutoSlugField(populate_from='title', max_length=255,
                         unique=True, always_update=True, blank=False)

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name_plural = 'categories'


class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    slug = AutoSlugField(populate_from='title', max_length=255,
                         unique=True, always_update=True, blank=False)
    description = models.TextField(max_length=3001, blank=True)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category', related_name='posts')
    tags = TaggableManager()

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('detail_post', args=[self.slug])