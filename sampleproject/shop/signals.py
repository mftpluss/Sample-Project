from django.db.models.signals import post_save,post_delete,pre_delete,pre_save
from django.dispatch import receiver # decorator that get every signal
from .models import Product,LogProduct,TempLogProudct

@receiver(post_save,sender=Product)
def log_product_save(sender,instance,created,**kwargs):
  if created:
    action = "Created"
  else:
    action = "Updated"
  LogProduct.objects.create(action=action,product_name=instance)

@receiver(post_delete,sender=Product)
def log_product_delete(sender,instance,**kwargs):
  LogProduct.objects.create(action="Deleted",product_name = instance)


@receiver(pre_delete,sender=Product)
def before_delete(sender,instance,**kwargs):
  TempLogProudct.objects.create(log_product="about pre delete")
