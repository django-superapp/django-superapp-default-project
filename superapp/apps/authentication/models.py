import json

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from guardian.mixins import GuardianUserMixin
from django.core import serializers


class User(AbstractUser, GuardianUserMixin):

    email = models.EmailField(_("email address"), blank=False, null=False, unique=True)

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    modified_at = models.DateTimeField(_("modified at"), auto_now=True)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        permissions = (
            ("can_view_dashboard", "Can view dashboard"),
            ("can_view_custom_page", "Can view custom page"),
        )

    def __str__(self):
        return self.email if self.email else self.username

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.last_name}, {self.first_name}"

        return None

    def to_json(self):
        return json.loads(serializers.serialize('json', [ self, ]))[0]['fields']

