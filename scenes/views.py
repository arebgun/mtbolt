from django.shortcuts import render_to_response, get_object_or_404
from scenes.models import Scene

def scene_details(request, scene_id):
    s = get_object_or_404(Scene, pk=scene_id)
    return render_to_response('scenes/scene_details.html', {'scene': s})
