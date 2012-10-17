from django.conf.urls import patterns, url

urlpatterns = patterns('tasks.views',
    url(r'^description/$', 'description'),
    url(r'^completed/$', 'completed', name='task_completed'),
)
