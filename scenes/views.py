from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib import messages
from scenes.models import Scene
from scenes.forms import FreeTextQuestionForm

def freetext_question(request):
    if request.method == 'POST':
        form = FreeTextQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            s = form.cleaned_data['scene']
            messages.success(request, 'Thanks!')
            return redirect('scene_details', s.pk)
        else:
            # the scene and entity ids SHOULD be in the post data
            s = Scene.objects.get(pk=request.POST['scene'][0])
            e = s.entities.get(pk=request.POST['entity'][0])
    else:
        # get a random scene and a random entity in the scene
        # NOTE this is very inefficient, but it's the easiest way to do it
        s = Scene.objects.order_by('?')[0]
        e = s.entities.order_by('?')[0]

        form = FreeTextQuestionForm(question='%s is' % e.name,
                                    initial={'scene': s.pk, 'entity': e.pk})

    data = {'scene': s, 'entity': e, 'form': form}
    return render_to_response('scenes/freetext_question.html', data,
                              context_instance=RequestContext(request))
