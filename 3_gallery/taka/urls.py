from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
		url(r'^$', 'gal.views.upload'),
		url(r'^lists$', 'gal.views.lists'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )