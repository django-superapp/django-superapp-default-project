from django.urls import path

from superapp.apps.sample_app.views import hello_world


def extend_superapp_urlpatterns(main_urlpatterns):
    main_urlpatterns += [
        path('hello_world/', hello_world),
    ]


def extend_superapp_admin_urlpatterns(main_admin_urlpatterns):
    main_admin_urlpatterns += [
        path('hello_world/', hello_world),
    ]
