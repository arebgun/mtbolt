from django.contrib import admin
from tasks.models import DescriptionTask, DescriptionQuestion

class DescriptionTaskAdmin(admin.ModelAdmin):
    search_fields = ('completion_code',)
    list_display = ('completion_code', 'approved')
    list_filter = ('approved', 'created', 'modified')

class DescriptionQuestionAdmin(admin.ModelAdmin):
    search_fields = ('answer',)
    list_filter = ('created', 'modified')

admin.site.register(DescriptionTask, DescriptionTaskAdmin)
admin.site.register(DescriptionQuestion, DescriptionQuestionAdmin)
