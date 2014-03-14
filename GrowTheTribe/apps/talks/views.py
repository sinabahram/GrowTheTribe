from django.template import loader

from django.contrib.auth import logout as auth_logout
from django.views.generic import CreateView, UpdateView, DeleteView, \
    DetailView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, get_object_or_404

from .models import Appearance, Talk, Conference
from .forms import TalkForm, ResourceFormSet, AppearanceFormSet


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('index')


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['latest_talk_list'] = \
            Appearance.objects.order_by('updated')[:5]
        context['latest_conference_list'] = \
            Conference.objects.order_by('updated')[:5]
        return context


class AppearanceCreate(CreateView):
    model = Appearance
    fields = '__all__'
    template_name = 'appear_form.html'


class AppearanceUpdate(UpdateView):
    model = Appearance
    fields = '__all__'
    template_name = 'appear_form.html'


class AppearanceDelete(DeleteView):
    model = Appearance
    success_url = reverse_lazy('appearance-list')
    template = loader.get_template('index.html')


class ManageTalksCombinedView(CreateView):
    template_name = 'manage_talks.html'
    form_class = TalkForm

    def get_context_data(self, **kwargs):
        context = \
            super(ManageTalksCombinedView, self).get_context_data(**kwargs)
        instance = None
        talk_pk = self.kwargs.get('pk')
        if talk_pk:
            instance = get_object_or_404(Talk, pk=talk_pk)
        if self.request.POST:
            context['form'] = TalkForm(self.request.POST, instance=instance)
            context['appearanceformset'] = AppearanceFormSet(self.request.POST,
                                                             instance=instance)
            context['resourceformset'] = ResourceFormSet(self.request.POST,
                                                         instance=instance)
        else:
            context['form'] = TalkForm(instance=instance)
            context['appearanceformset'] = AppearanceFormSet(instance=instance)
            context['resourceformset'] = ResourceFormSet(instance=instance)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form = context['form']
        appearanceformset = context['appearanceformset']
        resourceformset = context['resourceformset']
        form.instance.user = self.request.user
        if form.is_valid() and appearanceformset.is_valid() and \
           resourceformset.is_valid():
            self.object = form.save()

            appearanceformset.instance = self.object
            resourceformset.instance = self.object
            appearanceformset.save()
            resourceformset.save()
            #return redirect(self.object.get_absolute_url())
            return super(ManageTalksCombinedView, self).form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ConferenceDetail(DetailView):
    model = Conference


class AppearanceDetail(DetailView):
    model = Appearance


class ProfileView(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['my_talks'] = Appearance.objects.all()
#         context['my_talks'] = Appearance.objects.get(user=self.request.user)
        return context
