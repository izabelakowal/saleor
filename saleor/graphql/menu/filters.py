import django_filters

from ...menu.models import Menu, MenuItem
from ..core.types import FilterInputObjectType
from ..utils import filter_by_query_param


def filter_menu_search(qs, _, value):
    menu_fields = ["name"]
    return filter_by_query_param(qs, value, menu_fields)


def filter_menu_item_search(qs, _, value):
    menu_item_fields = ["name"]
    return filter_by_query_param(qs, value, menu_item_fields)


class MenuFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method=filter_menu_search)

    class Meta:
        model = Menu
        fields = ["search"]


class MenuItemFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method=filter_menu_item_search)

    class Meta:
        model = MenuItem
        fields = ["search"]


class MenuFilterInput(FilterInputObjectType):
    class Meta:
        filterset_class = MenuFilter


class MenuItemFilterInput(FilterInputObjectType):
    class Meta:
        filterset_class = MenuItemFilter
