from django.conf.urls import patterns, url

urlpatterns = patterns('object_tasks.views',
    url(r'^description/$', 'description'),
    url(r'^completed/$', 'completed', name='task_completed'),
)
