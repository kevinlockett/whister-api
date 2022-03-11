from django.db import models

class ServiceInvoice(models.Model):
    invoice = models.ForeignKey("Invoice", on_delete=models.CASCADE)
    service = models.ForeignKey("Service", on_delete=models.CASCADE)