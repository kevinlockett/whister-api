from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from whistlerapi.views import register_user, login_user

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login_user),
    path('register', register_user),
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
