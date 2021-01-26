import datetime
from django import template


register = template.Library()


@register.simple_tag
def current_date(format_string):
    return datetime.datetime.utcnow().strftime(format_string)


@register.simple_tag
def reverse_string(string):
    return string[::-1]
