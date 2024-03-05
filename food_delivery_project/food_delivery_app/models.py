from django.db import models

# Create your models here.
class customer_details(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.TextField()
    order_history = models.TextField()
    preferences = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name