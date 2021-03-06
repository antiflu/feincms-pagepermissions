from django import template

from pagepermissions.extension import has_permission_to_view

register = template.Library()

@register.filter
def check_nav_permission(page, request):
  return has_permission_to_view(page, request.user)
 
