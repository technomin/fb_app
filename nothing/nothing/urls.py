from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'me.views.authorize_application', name='authorize_application'),
    url(r'^manag_pages$', 'me.views.get_token', name='get_token'),
    )