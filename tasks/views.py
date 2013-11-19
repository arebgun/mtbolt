from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.conf import settings
from django.db.models import Count
from scenes.models import Entity
from tasks.models import DescriptionTask, DescriptionQuestion
from random import choice

def completed(request):
    completion_code = request.session.get('completion_code', None)
    if completion_code:
        del request.session['completion_code']
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
            # ans = request.POST['q%d_ans'%i]
            # object_description = request.POST['q%d_obj'%i]
            location_description = request.POST['q%d_loc'%i]
            e = Entity.objects.get(pk=eid)
            entities.append(e)
            q = DescriptionQuestion(scene=e.scene, entity=e, object_description='', location_description=location_description)
            questions.append(q)

        task = DescriptionTask()
        # save task to get task.id
        task.save()
        task.questions = questions
        # save again including answers
        task.save()
        request.session['completion_code'] = task.completion_code
        return redirect('task_completed')
    else:
        # sort entities by increasing number of answers
        # shuffle first, so that if two people start at the same time they
        # have a lesser chance of working on the same entities
        # NOTE this is very inefficient, but its the easiest way to do it
        # entities = Entity.objects \
        #     .filter(generated_descriptions__corpus_size=300) \
        #     .annotate(ans_count=Count('descriptions')) \
        #     .order_by('?', 'ans_count')[:settings.BOLT_QUESTIONS_PER_TASK]

        entities = Entity.objects \
            .annotate(ans_count=Count('descriptions')) \
            .order_by('?', 'ans_count')[:settings.BOLT_QUESTIONS_PER_TASK]

        student_desc = [choice(e.generated_descriptions.filter(corpus_size=settings.CORPUS_SIZE, representation_model=settings.REPRESENTATION_MODEL)) for e in entities]

        #entities = Entity.objects.filter(generated_descriptions__corpus_size=300).values('scene', 'name', 'generated_descriptions__corpus_size', 'generated_descriptions__representation_model').annotate(ans_count=Count('descriptions')).order_by('?', 'ans_count')[:5]

    return render_to_response('tasks/description.html',
                              {'entities': zip(entities, student_desc)},
                              context_instance=RequestContext(request))
