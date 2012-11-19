from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.conf import settings
from django.db.models import Count
from scenes.models import Entity
from tasks.models import DescriptionQuestion
from object_tasks.models import ObjectDescriptionTask, EntityBinding

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
        descriptions = DescriptionQuestion.objects.filter(use_in_object_tasks=True)\
                .annotate(binding_count=Count('entity_bindings'))\
                .order_by('?', 'binding_count')[:settings.BOLT_OBJECT_QUESTIONS_PER_TASK]
    return render_to_response('object_tasks/description.html',
                              {'descriptions': descriptions},
                              context_instance=RequestContext(request))
