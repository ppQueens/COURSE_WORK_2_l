from django import template
register = template.Library()

@register.filter
def replace(value, old, new):
    return str(value).replace(old, new)
