from django.shortcuts import render

# Create your views here.
def simple_ifelse(request):
    d={'a':10,'b':20}
    return render(request,'sec_ifelse.html',d)