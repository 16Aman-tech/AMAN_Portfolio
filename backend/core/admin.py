from django.contrib import admin
from .models import Profile, Experience


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "role")
    fieldsets = (
        ("Basic Info", {
            "fields": (
                "name",
                "role",
                "hero_bio",
                "about_bio",
            )
        }),

        ("Contact", {
            "fields": (
                "email",
                "phone",
                "location",
                "github",
                "linkedin",
            )
        }),

        ("Files", {
            "fields": (
                "resume",
                "image",
                "about_image",
            )
        }),
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("company", "role", "duration", "order")