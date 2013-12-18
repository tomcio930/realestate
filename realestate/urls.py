from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from realestate.settings import MEDIA_ROOT, MEDIA_URL
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'realestate.views.home', name='home'),
    # url(r'^realestate/', include('realestate.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'', include(admin.site.urls))
    #url(r'images/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': MEDIA_ROOT, 'show_indexes': True})
) + static(MEDIA_URL, document_root=MEDIA_ROOT)
