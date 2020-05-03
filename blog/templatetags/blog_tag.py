from django import template
# from ..models import Category

register = template.Library()


# @register.simple_tag(takes_context=True)
# def get_categories(count=None, order='-name'):
#     from blog.models import Category
#     categories = Category.objects.filter(to_display=True).order_by(order)
#     if count is not None:
#         categories = categories[:count]
#     return categories


@register.simple_tag()
def categories_navbar(count=None):
    from blog.models import Category
    categories = Category.objects.filter(to_display=True).order_by('-name')
    if count is not None:
        categories = categories[:count]
        return categories


@register.simple_tag()
def get_categories():
    from blog.models import Category
    return Category.objects.filter(to_display=True).order_by('-name')

