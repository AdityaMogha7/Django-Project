from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    #context are set of varibales that are sent to the templates.
    context={
        "variable1":"Hello World",
        "variable2":"Hello Guyss"
    }
    return render(request,"index.html",context)
    #return HttpResponse("This is Homepage")

def about(request):
    return HttpResponse("This is About")

def services(request):
    return HttpResponse("This is Services")

def contact(request):
    return HttpResponse("This is Contact")