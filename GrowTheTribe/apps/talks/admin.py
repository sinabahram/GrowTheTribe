from django.contrib import admin
from .models import Conference
from .models import Appearance
from .models import Resource


# Register your models here.
admin.site.register(Conference)
admin.site.register(Appearance)
admin.site.register(Resource)
