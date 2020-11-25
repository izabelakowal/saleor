import django_filters

from ...webhook.models import Webhook
from ..core.types import FilterInputObjectType
from ..utils import filter_by_query_param


def filter_webhook_search(qs, _, value):
    page_fields = ["name", "target_url"]
    return filter_by_query_param(qs, value, page_fields)


class WebhookFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method=filter_webhook_search)
    is_active = django_filters.BooleanFilter()

    class Meta:
        model = Webhook
        fields = ["search", "is_active"]


class WebhookFilterInput(FilterInputObjectType):
    class Meta:
        filterset_class = WebhookFilter
