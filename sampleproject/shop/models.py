from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=10,decimal_places=0)
  stock = models.IntegerField()

  def __str__(self):
    return self.name
######################################################
# middleware
class LogProduct(models.Model):
  action = models.CharField(max_length=50)
  product_name = models.CharField(max_length=100)
  ip_address = models.GenericIPAddressField(null=True,blank=True)
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.action} - {self.product_name} - {self.timestamp}"