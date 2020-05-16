from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def blog(request):
    return render (request,"blog.html")