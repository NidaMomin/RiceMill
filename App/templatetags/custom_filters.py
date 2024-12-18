from django import template

register = template.Library()

@register.filter(name='as_p')
def as_p(value):
    return f"<p>{value}</p>"
