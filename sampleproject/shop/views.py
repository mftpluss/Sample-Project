from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
import sweetify

sweetify.DEFAULT_OPTS = {
    'showConfirmButton': True,
    'timer': 4000,
    'allowOutsideClick': True,
    'confirmButtonText': 'OK',
}


# Create your views here.
def index(request):
  return HttpResponse("hello world this is index page")

def add_admin(request):
  if request.method == "POST":
      username_input = request.POST.get("username-input")
      password_input = request.POST.get("password-input")
      user = User.objects.create_user(username=username_input,password=password_input,is_staff=True)
      user.save()
      sweetify.success(request,title="Successfully message !",text="Successfully added admin !",icon="success")
      return redirect("add_admin")
  return render(request,"shop/add-admin.html")