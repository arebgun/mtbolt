from django.contrib import admin
from scenes.models import Scene, Entity, GeneratedDescription

class EntityInline(admin.TabularInline):
    model = Entity

class SceneAdmin(admin.ModelAdmin):
    inlines = (EntityInline,)
    search_fields = ('name',)
    list_filter = ('created', 'modified')

admin.site.register(Scene, SceneAdmin)
