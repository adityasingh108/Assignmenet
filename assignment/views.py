from django import http
from django.http import HttpResponse
from django.shortcuts import render ,redirect



def home(request):
    return HttpResponse('''<h3><a href="/post"> Create Your  Post</a></h3> <br> <h3><a href="/product"> Create Your Product</a></h3>''')