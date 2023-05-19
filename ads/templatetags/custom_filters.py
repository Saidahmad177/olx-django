from django import template

register = template.Library()


@register.filter
def replace_comma(value):
    return value.replace(",", " ")
