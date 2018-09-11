from django import template

register = template.Library()


@register.filter()
def to_int(value):
    return range(value)


@register.filter()
def to_remaining(value):
    value = 5 - value
    return range(value)


@register.filter()
def increment(value):
    value = value + 1
    return range(value)
