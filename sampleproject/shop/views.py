from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("hello world this is index page")

def add_admin(request):
  return render(request,"shop/add-admin.html")