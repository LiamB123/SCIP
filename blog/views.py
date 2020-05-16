from django.shortcuts import render , redirect , HttpResponse 

# Create your views here.
def blog(request):
    return HttpResponse("BLOG")