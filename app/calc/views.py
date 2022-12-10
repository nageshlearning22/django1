from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello World<h1>")


def hometemplate(request):
   return  render(request,'index.html')

def telcalc(request):
   return  render(request,'calculator.html',{'name':'Ramya'})

def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res= val1 + val2
    return render(request,'AddResult.html',{'result': res})