from django.shortcuts import render,HttpResponse
from myapp.models import Contact
# Create your views here.
def index(request):
    # return HttpResponse("THis is my app")
    context ={
        "pageName": "Home Page",
    }
    return render(request, 'home.html', context)

def about(reques):
    return HttpResponse("THis is my about page")

def contact(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request, 'contact.html')