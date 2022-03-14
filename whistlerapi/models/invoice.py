from django.db import models
from django.contrib.auth.models import User

class Invoice(models.Model):
    customer = models.ForeignKey(
        "AppUser", on_delete=models.CASCADE, related_name='invoices')
    services = models.ManyToManyField(
        "Service", through="ServiceInvoice", related_name='invoices')
    service_date = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(null=True, blank=True)
    payment_type = models.ForeignKey(
        "PaymentType", on_delete=models.CASCADE, null=True, blank=True)

    @property
    def total(self):
        return sum([p.price for p in self.services.all()], 0)

    def __str__(self):
        is_open = 'Completed' if self.completed_on else 'Open'
        return f'{is_open} order for {self.customer.get_full_name()}'
