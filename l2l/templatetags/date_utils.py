from django import template

register = template.Library()


@register.filter
def format_date(date_string):
    return date_string.replace("T", " ")
