from django.shortcuts import render



def home(request):
    print("home function is called views")  
    return render (request,"home.html")
   
    #return HttpResponse ("<h1>Hello this index page</h1>")
   # return render(request,"home.html",)

def about(request):
    #return HttpResponse("<h1> This is about page</h1>")
  return render (request,"about.html")


def Services(request):
   #return HttpResponse("<h1> this is category page </h1> ")
  
   return render (request,"services.html")

def career_emp(request):
    #return HttpResponse("<h1> this is Services page </h1> ")
    
    return render (request,"career_emp.html")