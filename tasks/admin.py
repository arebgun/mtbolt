from django.contrib import admin
from tasks.models import DescriptionTask, DescriptionQuestion

class DescriptionTaskAdmin(admin.ModelAdmin):
    search_fields = ('cofirmation_code',)
    list_filter = ('created', 'modified')

class DescriptionQuestionAdmin(admin.ModelAdmin):
    search_fields = ('answer',)
    list_filter = ('created', 'modified')

admin.site.register(DescriptionTask, DescriptionTaskAdmin)
admin.site.register(DescriptionQuestion, DescriptionQuestionAdmin)
