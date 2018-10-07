from django import template
from ..models import Record

register = template.Library()


@register.simple_tag
def get_categories():

    return Record.objects.all()

