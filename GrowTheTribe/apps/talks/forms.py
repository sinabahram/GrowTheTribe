from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import Talk, Appearance, Resource


class TalkForm(ModelForm):
    class Meta:
        model = Talk


class AppearanceForm(ModelForm):
    class Meta:
        model = Appearance


class ResourceForm(ModelForm):
    class Meta:
        model = Resource

ResourceFormSet = inlineformset_factory(Talk, Resource, extra=1)
AppearanceFormSet = inlineformset_factory(Talk, Appearance, extra=1)
