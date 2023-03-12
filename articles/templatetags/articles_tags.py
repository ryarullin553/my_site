from django import template
from articles.models import *

register = template.Library()


@register.inclusion_tag('articles/tags/categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}
