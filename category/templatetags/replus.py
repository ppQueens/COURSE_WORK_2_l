from django import template
register = template.Library()

@register.filter
def replus(value):
    return value.replace("+","_")

