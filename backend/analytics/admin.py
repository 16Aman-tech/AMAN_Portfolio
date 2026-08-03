from django.contrib import admin
from .models import Visitor, ResumeDownload


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):

    list_display = (
        "ip_address",
        "visited_at",
    )

    list_filter = (
        "visited_at",
    )

    search_fields = (
        "ip_address",
    )

    ordering = (
        "-visited_at",
    )


@admin.register(ResumeDownload)
class ResumeDownloadAdmin(admin.ModelAdmin):

    list_display = (
        "ip_address",
        "downloaded_at",
    )

    list_filter = (
        "downloaded_at",
    )

    search_fields = (
        "ip_address",
    )

    ordering = (
        "-downloaded_at",
    )