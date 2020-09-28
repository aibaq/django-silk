from django.contrib import admin

from silk.models import (
    Request,
    Response,
)


class ResponseInlineAdmin(admin.TabularInline):
    model = Response


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    inlines = [ResponseInlineAdmin]
    ordering = ('-start_time', )
    list_display = (
        'username', 'path', 'method', 'start_time', 'view_name', 'meta_time',
        'meta_num_queries', 'meta_time_spent_queries', )
    search_fields = ('raw_body', 'body', 'path', 'username')
    list_filter = (
        'path', 'method', 'start_time', 'view_name', 'response__status_code')
    show_full_result_count = False
