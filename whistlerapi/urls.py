from rest_framework.routers import DefaultRouter
from django.urls import include, path
from whistlerapi import views

router = DefaultRouter(trailing_slash=False)
router.register(r'appusers', views.AppUserView, 'app_user')
router.register(r'instruments', views.InstrumentView, 'instrument')
router.register(r'instrumentfamilies', views.InstrumentFamilyView, 'instrument_family')
router.register(r'invoices', views.InvoiceView, 'invoice')
router.register(r'musicstyles', views.MusicStyleView, 'music_style')
router.register(r'roles', views.RoleView, 'role')
router.register(r'paymenttypes', views.PaymentTypeView, 'payment_type')
router.register(r'services', views.ServiceView, 'service')
router.register(r'shops', views.ShopView, 'shop')
router.register(r'states', views.StateView, 'state')


urlpatterns = [
    path('', include(router.urls)),
]