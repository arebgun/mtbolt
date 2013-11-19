import os
import uuid
from django.db import models
from mtbolt.models import CommonInfo

def get_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('scenes', filename)

class Scene(CommonInfo):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=get_image_path)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('scene_details', (self.id,))

class Entity(CommonInfo):
    scene = models.ForeignKey(Scene, related_name='entities')
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'entities'

    def __unicode__(self):
        return self.name

class GeneratedDescription(CommonInfo):
    entity = models.ForeignKey(Entity, related_name='generated_descriptions')
    text = models.CharField(max_length=200)
    corpus_size = models.IntegerField()
    representation_model = models.CharField(max_length=6)

    class Meta:
        verbose_name_plural = 'generated_descriptions'

    def __unicode__(self):
        return self.text
