from django import template
from category import translates_word
register = template.Library()

@register.filter
def get_by_key(dictio, value):
    return dictio.get(value, value)
