from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def third(request):
    return HttpResponse('<i>THIS IS ID OF THE VIEW</i>')

def forth(request):
    return HttpResponse('<i><h1><marquee>THIS IS ONE OF THE SPECIFIC GENERIC</marquee></h1></i>')
    
    