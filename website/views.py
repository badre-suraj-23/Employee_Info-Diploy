from django.shortcuts import render

# Create your views here.
def home(request):
    print("home function is called views")  
    return render (request,"home.html")