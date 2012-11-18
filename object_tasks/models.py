from django.db import models
from mtbolt.models import CommonInfo
import uuid

class DescriptionTask(CommonInfo):
    completion_code = models.CharField(max_length=32,
                                       unique=True,
                                       default=lambda:uuid.uuid4().hex)
    approved = models.NullBooleanField()

    def __unicode__(self):
        return self.completion_code

class EntityBinding(CommonInfo):
    task = models.ForeignKey(DescriptionTask, related_name='entity_bindings')
    scene = models.ForeignKey('scenes.Scene', related_name='entity_bindings')
    entity = models.ForeignKey('scenes.Entity', related_name='bindings')
    description = models.ForeignKey('tasks.DescriptionQuestion')

    binding = models.IntegerField()

    def __unicode__(self):
        return "%s %s" % (self.description, self.binding)
