from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.conf import settings
from django.db.models import Count
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
        bindings = []
        num_questions = int(request.POST['num_questions'])
        for i in xrange(1, num_questions+1):
            did = request.POST['q%d_did'%i]
            object_binding = int(request.POST['q%d_bin'%i])
            d = DescriptionQuestion.objects.get(pk=did)
            b = EntityBinding(description=d, binding=object_binding)
            bindings.append(b)
        task = ObjectDescriptionTask()
        # save task to get task.id
        task.save()
        task.entity_bindings = bindings
        # save again including answers
        task.save()
        request.session['completion_code'] = task.completion_code
        return redirect('task_completed')
    else:
        descriptions = DescriptionQuestion.objects.filter(use_in_object_tasks=True)\
                .annotate(binding_count=Count('entity_bindings'))\
                .order_by('binding_count', '?')[:settings.BOLT_OBJECT_QUESTIONS_PER_TASK]
    return render_to_response('object_tasks/description.html',
                              {'descriptions': descriptions},
                              context_instance=RequestContext(request))
