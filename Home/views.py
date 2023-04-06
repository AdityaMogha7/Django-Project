from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is Homepage")

def about(request):
    return HttpResponse("This is About")

def services(request):
    return HttpResponse("This is Services")

def contact(request):
    return HttpResponse("This is Contact")