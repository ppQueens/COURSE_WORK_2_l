from django import template
from category import translates_word
register = template.Library()

@register.filter
def for_human_reading(value):
    return translates_word.fields.get(value)
