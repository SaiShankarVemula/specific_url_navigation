from django.shortcuts import render

# Create your views here.

def bawarchi(request):
    return render(request,'bawarchi.html')