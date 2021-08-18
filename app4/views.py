from django.shortcuts import render

# Create your views here.
def simple_nestedif(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'fo_nestedif.html',d)