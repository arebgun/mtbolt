from django.contrib import admin
from django.conf.urls import patterns
from tasks.models import DescriptionTask, DescriptionQuestion
import csv
from django.http import HttpResponse

def approve(modeladmin, request, queryset):
    queryset.update(approved=True)
approve.short_description = 'Approve selected decription tasks'

def reject(modeladmin, request, queryset):
    queryset.update(approved=False)
reject.short_description = 'Reject selected decription tasks'

def use(modeladmin, request, queryset):
    queryset.update(use_in_object_tasks=True)
use.short_description = 'Use selected description questions in object tasks'

def do_not_use(modeladmin, request, queryset):
    queryset.update(use_in_object_tasks=False)
do_not_use.short_description = 'Do not use selected description questions in object tasks'

class DescriptionTaskAdmin(admin.ModelAdmin):
    fields = ('completion_code', 'approved')
    readonly_fields = ('completion_code',)
    search_fields = ('completion_code',)
    list_display = ('completion_code', 'approved')
    list_filter = ('approved', 'created', 'modified')
    actions = [approve, reject]

class DescriptionQuestionAdmin(admin.ModelAdmin):
    list_display = ('scene', 'entity', 'object_description', 'location_description', 'answer', 'use_in_object_tasks',)
    list_filter = ('created', 'modified', 'scene', 'task')

    actions = [use, do_not_use]

    def get_urls(self):
        urls = super(DescriptionQuestionAdmin, self).get_urls()
        my_urls = patterns('',
                           (r'^responses/$', self.responses_view)
                          )
        return my_urls + urls

    def responses_view(self, request):
        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename="responses.csv"'

        writer = csv.writer(response)
        writer.writerow(['scene', 'entity', 'object_description', 'location_description', 'old_description', 'completion_code', 'approved'])
        for dq in DescriptionQuestion.objects.all():
            writer.writerow([dq.scene.name, dq.entity.name, dq.object_description, dq.location_description, dq.answer, dq.task.completion_code, dq.task.approved])

        return response

admin.site.register(DescriptionTask, DescriptionTaskAdmin)
admin.site.register(DescriptionQuestion, DescriptionQuestionAdmin)
