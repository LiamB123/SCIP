from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.
def blog(request):
    return render (request,"blog/blog.html")
