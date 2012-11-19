from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mtbolt.views.home', name='home'),
    # url(r'^mtbolt/', include('mtbolt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'scenes/', include('scenes.urls')),
    # object tasks has to come first, because I'm bad at naming apps, and tasks also matches object_tasks
    url(r'object_tasks/', include('object_tasks.urls')),
    url(r'tasks/', include('tasks.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
