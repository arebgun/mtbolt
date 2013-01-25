from django.db import models
from mtbolt.models import CommonInfo
import uuid

class ObjectDescriptionTask(CommonInfo):
    completion_code = models.CharField(max_length=32,
                                       unique=True,
                                       default=lambda:uuid.uuid4().hex)
    approved = models.NullBooleanField()

    def __unicode__(self):
        return self.completion_code

class EntityBinding(CommonInfo):
    # the ObjectDescriptionTask that contains this response
    task = models.ForeignKey(ObjectDescriptionTask, related_name='entity_bindings')

   # the response from the first experiment, which is shown to the user for proofing
    description = models.ForeignKey('tasks.DescriptionQuestion', related_name='entity_bindings')

    # an integer representing the object the user selects as described by description
    binding = models.IntegerField()

    def actual_object_name(entity_binding):
        return entity_binding.description.entity.name

    def __unicode__(self):
        return "%s %s" % (self.description, self.binding)
