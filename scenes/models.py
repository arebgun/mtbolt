from django.db import models
from mtbolt.models import CommonInfo

class Scene(CommonInfo):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='scenes')

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
