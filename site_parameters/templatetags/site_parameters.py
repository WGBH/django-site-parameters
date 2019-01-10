from django import template
from ..helpers import find_site_parameter
from ..models import SiteNavigationSectionItem

register = template.Library()

@register.simple_tag
def lookup_site_parameter(param_type, slug, *args, **kwargs):
    default = None
    if 'default' in kwargs.keys():
        default = kwargs['default']
    value = find_site_parameter(slug=slug, param_type=param_type, default=default)
    return value
    
@register.simple_tag
def build_navigation_menu(slug, *args, **kwargs):
    nav_items = SiteNavigationSectionItem.objects.filter(navigation_menu__slug=slug).filter(order_in_menu__gt=0).order_by('-order_in_menu')
    return nav_items
    