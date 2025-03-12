from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(LogProduct)
admin.site.register(TempLogProudct)
admin.site.register(Access)
admin.site.register(AdminProfile)
admin.site.register(Role)