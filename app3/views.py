from django.shortcuts import render

# Create your views here.
def simple_elif(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'thi_elif.html',d)