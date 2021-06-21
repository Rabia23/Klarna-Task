"""Api filters file."""
from django_filters import FilterSet, filters

from apps.api.models import FunctionLogs


class FunctionLogsFilter(FilterSet):
    """Function logs filter class.

    A filtering class that provides filters on the given data.

    Parameters
    ----------
    FilterSet : django_filters
    """

    function = filters.CharFilter(field_name="name", lookup_expr="exact")

    class Meta:  # noqa: D106
        model = FunctionLogs
        fields = ["function"]
