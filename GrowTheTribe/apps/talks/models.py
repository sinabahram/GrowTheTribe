from django.db.models import Model, CharField, DateField, URLField, \
    DateTimeField, TextField, ForeignKey, permalink, IntegerField
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


class Conference(Model):
    title = CharField(max_length=300)
    start_date = DateField('conference start date')
    end_date = DateField('conference end date')
    city = CharField(max_length=300)
    state = CharField(max_length=300, help_text="State / Province / District")
    country = CharField(max_length=300, default="USA")
    conference_home_url = URLField()
    tags = TaggableManager(blank=True)
    short_name = CharField(max_length=30, blank=True)
    twitter_hashtag = CharField(max_length=30, blank=True)
    accessibility_needed_votes = IntegerField(editable=False, blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    @property
    def name(self):
        return self.title

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('conference_detail', [self.pk])


class Talk(Model):
    type_choices = (('workshop', 'Workshop'),
                    ('presentation', 'Presentation'),
                    ('poster', 'Poster Presentation'),
                    ('panel', 'Panel Discussion'))
    title = CharField(max_length=300)
    type = CharField(max_length=12, choices=type_choices)
    description = TextField(blank=True)
    tags = TaggableManager(blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    user = ForeignKey(User, editable=False)

    @property
    def name(self):
        return self.title

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('index', None)

    @permalink
    def edit_view(self):
        return ('edit_talk', [self.pk])


class Appearance(Model):
    talk = ForeignKey(Talk)
    conference = ForeignKey(Conference)
    date = DateField('presentation date')
    authors = TextField()
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    @property
    def name(self):
        return '-'.join(
            [self.talk.title, str(self.date)])

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ('appearance_detail', [self.pk])


class Resource(Model):
    talk = ForeignKey(Talk)
    title = CharField(max_length=300)
    description = TextField()
    url = URLField()
    tags = TaggableManager()
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    @property
    def name(self):
        return self.title

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('resource_detail', [self.pk])
