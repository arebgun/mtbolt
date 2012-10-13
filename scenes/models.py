from django.db import models

class Scene(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='scenes')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('scenes.views.scene_details', (), {
            'scene_id': self.id
        })

class Entity(models.Model):
    scene = models.ForeignKey(Scene, related_name='entities')
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
