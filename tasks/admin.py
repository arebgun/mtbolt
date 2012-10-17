from django.contrib import admin
from tasks.models import DescriptionTask, DescriptionQuestion

admin.site.register(DescriptionTask)
admin.site.register(DescriptionQuestion)
