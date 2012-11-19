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

class DescriptionQuestion(CommonInfo):
    task = models.ForeignKey(DescriptionTask, related_name='questions')
    scene = models.ForeignKey('scenes.Scene')
    entity = models.ForeignKey('scenes.Entity', related_name='descriptions')
    answer = models.CharField(max_length=200)

    object_description = models.CharField(max_length=200)
    location_description = models.CharField(max_length=200)

    use_in_object_tasks = models.NullBooleanField()

    def __unicode__(self):
        return "%s %s %s" % (self.answer, self.object_description, self.location_description)
