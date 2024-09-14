from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("THis is my app")
    return render(request, 'home.html')

def about(reques):
    return HttpResponse("THis is my about page")
