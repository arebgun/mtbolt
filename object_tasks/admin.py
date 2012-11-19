from django.contrib import admin
from object_tasks.models import ObjectDescriptionTask, EntityBinding

def approve(modeladmin, request, queryset):
    queryset.update(approved=True)
approve.short_description = 'Approve selected decription tasks'

def reject(modeladmin, request, queryset):
    queryset.update(approved=False)
reject.short_description = 'Reject selected decription tasks'

class ObjectDescriptionTaskAdmin(admin.ModelAdmin):
    fields = ('completion_code', 'approved')
    readonly_fields = ('completion_code',)
    search_fields = ('completion_code',)
    list_display = ('completion_code', 'approved')
    list_filter = ('approved', 'created', 'modified')
    actions = [approve, reject]

class EntityBindingAdmin(admin.ModelAdmin):
    list_display = ('task', 'description', 'binding',)
    list_filter = ('created', 'modified', 'task')

admin.site.register(ObjectDescriptionTask, ObjectDescriptionTaskAdmin)
admin.site.register(EntityBinding, EntityBindingAdmin)
