from django.db import models

class Scene(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='scenes')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('scene_details', (self.id,))

class Entity(models.Model):
    scene = models.ForeignKey(Scene, related_name='entities')
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class FreeTextQuestion(models.Model):
    scene = models.ForeignKey(Scene, related_name='freetext_questions')
    entity = models.ForeignKey(Entity, related_name='freetext_questions')
    answer = models.CharField(max_length=200)

    def __unicode__(self):
        return self.answer
