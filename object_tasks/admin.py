from django.contrib import admin
from tasks.models import DescriptionTask, DescriptionQuestion

def approve(modeladmin, request, queryset):
    queryset.update(approved=True)
approve.short_description = 'Approve selected decription tasks'

def reject(modeladmin, request, queryset):
    queryset.update(approved=False)
reject.short_description = 'Reject selected decription tasks'

class DescriptionTaskAdmin(admin.ModelAdmin):
    fields = ('completion_code', 'approved')
    readonly_fields = ('completion_code',)
    search_fields = ('completion_code',)
    list_display = ('completion_code', 'approved')
    list_filter = ('approved', 'created', 'modified')
    actions = [approve, reject]

class DescriptionQuestionAdmin(admin.ModelAdmin):
    list_display = ('scene', 'entity', 'object_description', 'location_description', 'answer',)
    list_filter = ('created', 'modified', 'scene', 'task')

admin.site.register(DescriptionTask, DescriptionTaskAdmin)
admin.site.register(DescriptionQuestion, DescriptionQuestionAdmin)
