from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.conf import settings
from scenes.models import Entity
from tasks.models import DescriptionTask, DescriptionQuestion

def completed(request):
    completion_code = request.session.get('completion_code', None)
    return render_to_response('tasks/completed.html', {
        'completion_code': completion_code,
    })

def description(request):
    if request.method == 'POST':
        entities = []
        questions = []
        num_questions = int(request.POST['num_questions'])
        for i in xrange(1, num_questions+1):
            eid = request.POST['q%d_eid'%i]
            ans = request.POST['q%d_ans'%i]
            e = Entity.objects.get(pk=eid)
            entities.append(e)
            q = DescriptionQuestion(scene=e.scene, entity=e, answer=ans)
            questions.append(q)
        task = DescriptionTask()
        task.save()
        task.questions = questions
        task.save()
        request.session['completion_code'] = task.completion_code
        return redirect('task_completed')
    else:
        entities = Entity.objects.order_by('?')[:settings.BOLT_QUESTIONS_PER_TASK]
    return render_to_response('tasks/description.html',
                              {'entities': entities},
                              context_instance=RequestContext(request))
