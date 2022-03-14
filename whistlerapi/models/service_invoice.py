from django.db import models

class ServiceInvoice(models.Model):
    invoice = models.ForeignKey(
        "Invoice", related_name='invoice', on_delete=models.CASCADE)
    service = models.ForeignKey(
        "Service", related_name='service', on_delete=models.CASCADE)
