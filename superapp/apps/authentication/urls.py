
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

def extend_superapp_urlpatterns(main_urlpatterns):
    main_urlpatterns += [
        path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
        path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    ]

def extend_superapp_admin_urlpatterns(main_admin_urlpatterns):
    pass