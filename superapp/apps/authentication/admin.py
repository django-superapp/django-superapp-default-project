from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_superapp.helpers import SuperAppModelAdmin
from django_superapp.sites import superapp_admin_site
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.decorators import display
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from .models import (
    User,
)

admin.site.unregister(Group)


@admin.register(User, site=superapp_admin_site)
class UserAdmin(BaseUserAdmin, SuperAppModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = [
        "display_header",
        "is_active",
        "display_staff",
        "display_superuser",
        "display_created",
    ]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {"fields": (("first_name", "last_name"),)},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
    readonly_fields = ["last_login", "date_joined"]

    @display(description=_("User"), header=True)
    def display_header(self, instance: User):
        return instance.full_name, instance.email or instance.username

    @display(description=_("Staff"), boolean=True)
    def display_staff(self, instance: User):
        return instance.is_staff

    @display(description=_("Superuser"), boolean=True)
    def display_superuser(self, instance: User):
        return instance.is_superuser

    @display(description=_("Created"))
    def display_created(self, instance: User):
        return instance.created_at


@admin.register(Group, site=superapp_admin_site)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass
