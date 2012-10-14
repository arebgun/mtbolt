from django.conf.urls import patterns, url
from django.views.generic import DetailView
from scenes.models import Scene

urlpatterns = patterns('scenes.views',
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Scene,
            template_name='scenes/scene_details.html'),
        name='scene_details'),
    url(r'^ftq/$', 'freetext_question'),
)
