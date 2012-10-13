from django.conf.urls import patterns, include, url

urlpatterns = patterns('scenes.views',
    url(r'^(?P<scene_id>\d+)/$', 'scene_details'),
)
