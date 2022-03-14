from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from whistlerapi.views import register_user, login_user, AppUserView

router = DefaultRouter(trailing_slash=False)
router.register(r'appusers', AppUserView, 'app_user')

urlpatterns = [
    path('', include(router.urls)),
    path('login', login_user),
    path('register', register_user),
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
