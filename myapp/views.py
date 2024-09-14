from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("THis is my app")
    context ={
        "pageName": "Home Page",
    }
    return render(request, 'home.html', context)

def about(reques):
    return HttpResponse("THis is my about page")
