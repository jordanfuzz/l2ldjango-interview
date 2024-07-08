from django import template
from datetime import datetime

register = template.Library()


@register.filter
def format_date(date):
    if isinstance(date, str):
        date_object = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
        return date_object.strftime("%Y-%m-%d %H:%M:%S")
    return date.strftime("%Y-%m-%d %H:%M:%S")