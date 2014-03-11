from django.conf.urls import patterns, url

from django.contrib.auth.decorators import login_required

from .views import index, ManageTalksCombinedView, logout

urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^add/$', login_required(ManageTalksCombinedView.as_view()),
        name='add_talk')
    # url(r'^edit/(?P<pk>\d+)$',
    #     login_required(ManageTalksCombinedView.as_view()),
    #     name='edit_talk')
)
