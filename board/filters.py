from datetime import datetime, timedelta
from rest_framework.filters import BaseFilterBackend
from rest_framework.response import Response

from AIFFEL_prj.utils import utc_to_asia_seoul_to_str


class BoardSearchFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        title = request.query_params.get("title", None)
        context = request.query_params.get("context", None)

        if title:
            queryset = queryset.filter(title__icontains=title)

        if context:
            queryset = queryset.filter(context__icontains=context)

        return queryset


class BoardReactionFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        begin = request.query_params.get("begin", None)
        end = request.query_params.get("end", None)

        if begin:
            begin_month = utc_to_asia_seoul_to_str(begin)
            queryset = queryset.filter(created_at__gte=begin_month)

        if end:
            end_month = utc_to_asia_seoul_to_str(end)
            queryset = queryset.filter(created_at__lte=end_month)

        return queryset
