from django import template

register = template.Library()

@register.filter
def short_name(value):
    return value.replace(" ","-").lower()

@register.filter
def rem_slash(value):
    return value.replace("/","/ ")
