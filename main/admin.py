from django.contrib import admin
from main.models import *
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    search_fields = ("contact",)
    ordering = ("contact",)

    fieldsets = (
        # (None, {"fields": ("contact", "password")}),
        (
            ("Personal info"),
            {"fields": ("first_name", "last_name", "contact", "staff_type")},
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "contact",
                    "password1",
                    "password2",
                    "staff_type",
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Entreprise)
admin.site.register(Entrepreneur)
admin.site.register(EntrepriseLocation)
admin.site.register(Initiative)
admin.site.register(FicheAutoEvaluation)
