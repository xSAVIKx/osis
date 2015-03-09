__author__ = 'Iurii Sergiichuk'

import json

from django.utils.safestring import mark_safe
from django.template import Library


register = Library()


@register.filter(is_safe=True)
def to_json(obj):
    return mark_safe(json.dumps(obj))