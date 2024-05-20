from django.contrib import admin
from django_superapp.helpers import SuperAppModelAdmin
from django_superapp.sites import superapp_admin_site

from superapp.apps.sample_app.models import SampleModel


@admin.register(SampleModel, site=superapp_admin_site)
class SampleModelAdmin(SuperAppModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')
    list_per_page = 20
    ordering = ('-created_at',)
