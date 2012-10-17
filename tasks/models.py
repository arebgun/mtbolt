from django.db import models
from mtbolt.models import CommonInfo
import uuid

class DescriptionTask(CommonInfo):
    completion_code = models.CharField(max_length=32,
                                       unique=True,
                                       default=lambda:uuid.uuid4().hex)

    def __unicode__(self):
        return self.completion_code

class DescriptionQuestion(CommonInfo):
    task = models.ForeignKey(DescriptionTask, related_name='questions')
    # scene = models.ForeignKey('scenes.Scene')
    entity = models.ForeignKey('scenes.Entity')
    answer = models.CharField(max_length=200)

    def __unicode__(self):
        return self.answer
