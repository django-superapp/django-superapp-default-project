Canvas Canvas
You are an expert in Python, Django, scalable web development, and Django SuperApp structure.

## Key Principles
- Prioritize readability, maintainability, and Django best practices (PEP 8 compliance).
- Modular structure: organize code using Django apps within SuperApp for clear separation and reuse.
- Leverage built-in Django features; avoid raw SQL, prefer Django ORM.

## Django SuperApp Structure
- Quickly bootstrap projects using pre-built standalone apps.
- Each app includes independent `settings.py` and `urls.py` automatically integrated by the SuperApp system.

### App Settings Integration
`superapp/apps/<app_name>/settings.py`
```python
def extend_superapp_settings(main_settings):
    main_settings['INSTALLED_APPS'] += ['superapp.apps.sample_app']
```

### App URLs Integration
`superapp/apps/<app_name>/urls.py`
```python
from django.urls import path
from superapp.apps.sample_app.views import hello_world

def extend_superapp_urlpatterns(main_urlpatterns):
    main_urlpatterns += [path('hello_world/', hello_world)]
```

### App-Specific Requirements
Each app can define its own Python dependencies in:
`superapp/apps/<app_name>/requirements.txt`

These requirements should be installed during deployment or development setup if the app is used. The SuperApp system may include tooling to auto-install these when apps are enabled.

## Django Guidelines
- Use CBVs for complex logic, FBVs for simple tasks.
- Keep business logic in models/forms; views should handle requests/responses only.
- Utilize built-in authentication and forms/models validation.
- Follow strict MVT separation.
- Implement middleware strategically for authentication, logging, caching.
- Error handling via built-in mechanisms; customize error pages.
- Leverage signals for decoupled logging/error handling.
- Do not update migrations in the `migrations` folder. Update migrations only if there are exceptions or issues inside of it.

## Admin Integration

### Use `django-unfold` and SuperApp admin site with Sidebar Navigation

- Admins must live in: `superapp/apps/<app_name>/admin/<model_name_slug>.py`
- Models must live in: `superapp/apps/<app_name>/models/<model_name_slug>.py`
- Signals must live in: `superapp/apps/<app_name>/signals/<model_name_slug>.py`
- Services must live in: `superapp/apps/<app_name>/services/<service_name>.py`
- Views must live in: `superapp/apps/<app_name>/views/<view_name>.py`
- Tasks must live in: `superapp/apps/<app_name>/tasks/<task_name>.py`
- Other things must live in: `superapp/apps/<app_name>/<other>/<view_name>.py`
- Usually each of the above folders will have an `__init__.py` file to make them packages or to export `__all__` so make sure to keep it up to date.
- Register using `superapp_admin_site` from `superapp.apps.admin_portal.sites`
- Use `SuperAppModelAdmin` based on `unfold.admin.ModelAdmin`
- Prefer `autocomplete_fields` for `ForeignKey` and `ManyToManyField`

### Add Admin Navigation

Each app should configure sidebar entries under `UNFOLD['SIDEBAR']['navigation']` in its `settings.py`.

Example:
```python
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

def extend_superapp_settings(main_settings):
    main_settings['INSTALLED_APPS'] += ['superapp.apps.sample_app']

    main_settings['UNFOLD']['SIDEBAR']['navigation'] = [
        {
            "title": _("Sample App"),
            "icon": "extension",
            "items": [
                {
                    "title": lambda request: _("Sample Models"),
                    "icon": "table_rows",
                    "link": reverse_lazy("admin:sample_app_samplemodel_changelist"),
                    "permission": lambda request: request.user.has_perm("sample_app.view_samplemodel"),
                },
            ]
        },
    ]
```
Place this logic inside `superapp/apps/<app_name>/settings.py` within `extend_superapp_settings()`.

Example: `superapp/apps/sample_app/admin/sample_model.py`
```python
from superapp.apps.admin_portal.admin import SuperAppModelAdmin
from superapp.apps.admin_portal.sites import superapp_admin_site
from .models import SampleModel

@admin.register(SampleModel, site=superapp_admin_site)
class SampleModelAdmin(SuperAppModelAdmin):
    list_display = ['slug', 'name', 'created_at', 'updated_at']
    search_fields = ['name__slug', 'slug']
    autocomplete_fields = ['name']
```

## Dependencies
- Django
- Django REST Framework (APIs)
- Celery (background tasks)
- Redis (caching/task queues)
- PostgreSQL/MySQL (production databases)
- django-unfold (admin UI)

## Performance & Security
- Optimize ORM queries (`select_related`, `prefetch_related`).
- Use caching framework (Redis/Memcached).
- Apply async views/background tasks (Celery).
- Enforce Django security best practices (CSRF, XSS, SQL injection protections).

## Translation Convention
- Make sure that every string which is displayed to the end user is using _('XXX') from Django.

Follow Django and SuperApp documentation for detailed practices.

## Environment Variables
Use `.env.local.example` and `.env.example` files to manage environment variables for local development, deployment templates, and Docker containers, respectively. The AI agent should take these into account when generating or configuring project settings.

