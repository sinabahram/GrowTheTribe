from django.contrib import admin
from .models import Conference
from .models import Appearance
from .models import Resource
from .models import Talk


# Register your models here.
admin.site.register(Conference)
admin.site.register(Appearance)
admin.site.register(Resource)
admin.site.register(Talk)
