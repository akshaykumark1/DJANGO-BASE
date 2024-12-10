from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add(request):
    l=["apple\n","banana\n","mango\n","grapes\n"]
    return HttpResponse(l)
