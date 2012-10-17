from django.contrib import admin
from scenes.models import Scene, Entity

class EntityInline(admin.TabularInline):
    model = Entity

class SceneAdmin(admin.ModelAdmin):
    inlines = [EntityInline]

admin.site.register(Scene, SceneAdmin)
