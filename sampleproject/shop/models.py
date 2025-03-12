from django.db import models
from django.contrib.auth.models import User

class Access(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return f"Access => {self.name}"

class Role(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return f"Role => {self.name}"



class AdminProfile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  role = models.OneToOneField(Role,on_delete=models.CASCADE)
  permissions = models.ManyToManyField(Access,blank=True)

  def __str__(self):
    return f"{self.user.username} - {self.role}"

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

class TempLogProudct(models.Model):
  name = models.CharField(max_length=100)
  # log_product = models.ForeignKey(LogProduct,on_delete=models.CASCADE)
  description = models.CharField(max_length=100)

  def __str__(self):
    return f"TEMP => {self.log_product.product_name }"