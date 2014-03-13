from django.contrib.admin.site import register
from .models import Conference
from .models import Appearance
from .models import Resource
from .models import Talk


register(Conference)
register(Appearance)
register(Resource)
register(Talk)
