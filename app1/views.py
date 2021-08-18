from django.shortcuts import render

# Create your views here.
def simple_if(request):
    d={'a':10}
    return render(request,'first_if.html',d)