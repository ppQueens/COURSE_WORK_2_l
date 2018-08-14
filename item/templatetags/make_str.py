from django import template
register = template.Library()

@register.filter
def make_str(value):
    return str(value)
