"""whistler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from whistlerapi.views import register_user, login_user, AppUserView

SchemaView = get_schema_view(
    openapi.Info(
        title="Whistler API",
        default_version='v1',
        description="An api for users to schedule and teach music lessons",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter(trailing_slash=False)
router.register(r'appusers', AppUserView, 'app_user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login_user),
    path('register', register_user),
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
        SchemaView.without_ui(cache_timeout=None), name='schema-json'),
    re_path(r'^swagger/$', SchemaView.with_ui('swagger',
        cache_timeout=None), name='schema-swagger-ui'),
]
