from django.shortcuts import redirect
from django.urls import path


def extend_superapp_urlpatterns(main_urlpatterns):
    main_urlpatterns += [
        path("", lambda request: redirect('admin:index'), name="token_obtain_pair"),
    ]


def extend_superapp_admin_urlpatterns(main_admin_urlpatterns):
    pass
