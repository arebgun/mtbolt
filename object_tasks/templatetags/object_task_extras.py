from django.template import Library

register = Library()

@register.filter
def description_entities(description):
    return description.scene.entities.order_by('name')
