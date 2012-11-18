from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.conf import settings
from django.db.models import Count
from scenes.models import Entity
import tasks.models
import object_tasks.models

def completed(request):
    completion_code = request.session.get('completion_code', None)
    if completion_code:
        del request.session['completion_code']
    return render_to_response('object_tasks/completed.html', {
        'completion_code': completion_code,
    })

def description(request):
    if request.method == 'POST':
        # foo
        True
    else:
        # bar
        True
    return render_to_response('object_tasks/description.html',
                              context_instance=RequestContext(request))
