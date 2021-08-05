from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from home.models import Contact
# Create your views here

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'index.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        # desc=request.POST.get("message")
        contact=Contact(name=name,email=email,date=datetime.today())
        contact.save()


    
    return render(request,'contact.html')