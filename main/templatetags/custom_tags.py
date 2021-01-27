import datetime
from django import template


register = template.Library()


@register.simple_tag
def current_date(format_string):
    return datetime.datetime.utcnow().strftime(format_string)


@register.filter(name='reverse_string')
def reverse_string(string):
    return string[::-1]
