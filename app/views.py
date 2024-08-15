from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def python(request):
    return HttpResponse('python is high level open sorce interpreted scripting language')
def sql(request):
    return HttpResponse('sql is structured quary language which is store date in the form of tables')
 
