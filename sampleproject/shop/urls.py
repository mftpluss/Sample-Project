from django.urls import path
from .views import *


urlpatterns = [
  path("",index,name="indexpage"),
  path("add-admin",add_admin,name="add_admin")
]