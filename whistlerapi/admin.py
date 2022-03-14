from django.contrib import admin
from whistlerapi import models

# Register your models here.
admin.site.register(models.AppUser)
admin.site.register(models.InstrumentFamily)
admin.site.register(models.Instrument)
admin.site.register(models.Invoice)
admin.site.register(models.Merchant)
admin.site.register(models.MusicStyle)
admin.site.register(models.PaymentType)
admin.site.register(models.Role)
admin.site.register(models.ServiceType)
admin.site.register(models.Service)
admin.site.register(models.Shop)
admin.site.register(models.State)
