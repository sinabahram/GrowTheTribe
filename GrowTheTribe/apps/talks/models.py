from django.db import models
from taggit.managers import TaggableManager


class Conference(models.Model):
    title = models.CharField(max_length=300)
    start_date = models.DateField('conference start date')
    end_date = models.DateField('conference end date')
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300,
                             help_text="State / Province / District")
    country = models.CharField(max_length=300)
    conference_home_url = models.URLField()
    tags = TaggableManager()
    short_name = models.CharField(max_length=30)
    twitter_hash = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def name(self):
        return self.title

    def __unicode__(self):
        return self.title

#     @models.permalink
#     def get_absolute_url(self):
#         return ('conference_detail', [self.pk])


class Talk(models.Model):
    type_choices = (
        ('workshop', 'Workshop'),
        ('presentation', 'Presentation'),
        ('poster', 'Poster Presentation'),
        ('panel', 'Panel Discussion'),
    )
    title = models.CharField(max_length=300)
    type = models.CharField(max_length=12, choices=type_choices)
    description = models.TextField()
    tags = TaggableManager()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def name(self):
        return title

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('index', None)


class Appearance(models.Model):
    talk = models.ForeignKey(Talk)
    conference = models.ForeignKey(Conference)
    date = models.DateField('presentation date')
    authors = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def name(self):
        return '-'.join(
            [self.talk.title, str(self.date)])

    def __unicode__(self):
        return self.name

#     @models.permalink
#     def get_absolute_url(self):
#         return ('appearance_detail', [self.pk])


class Resource(models.Model):
    talk = models.ForeignKey(Talk)
    title = models.CharField(max_length=300)
    description = models.TextField()
    link = models.URLField()
    tags = TaggableManager()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def name(self):
        return self.title

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('resource_detail', [self.pk])
