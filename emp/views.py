from django.shortcuts import render, redirect,HttpResponse
from.models import Emp


def emp_home(request):
    return render(request, "emp/home.html", {})
def emp_view(request):
   
   emps=Emp.objects.all()
   return render(request,"emp_view.html",{'emps':emps})

def follow(request):
   return render(request,"follow.html")


def add_emp(request):
    if request.method == "POST":
        # Fetch data from POST request
        emp_name = request.POST.get("emp-name")
        emp_id = request.POST.get("emp-id")
        emp_age = request.POST.get("emp-age")
        emp_phone_no = request.POST.get("phone-no")  
        emp_address = request.POST.get("emp-address")
        emp_working = request.POST.get("emp-working")
        emp_department = request.POST.get("emp-department")
        


        # Create model object and set the data
        e = Emp()
        e.emp_name = emp_name
        e.emp_id = emp_id
        e.emp_age = emp_age
        e.emp_phone_no = emp_phone_no
        e.emp_address = emp_address
        e.emp_department = emp_department
        e.emp_working = bool(emp_working)  
        
        if emp_working is None:
          e.emp_working=False
        else:
          e.emp_working=True

        # Save the object
        e.save()

         #Redirect to home
        return redirect( "/")
    #  return redirect("/emp/home/")
    
    return render(request,"emp/add_emp.html", {})
# dele te button
def delete_emp(request,emp_id):
     print(emp_id)
     emp=Emp.objects.get(pk=emp_id)
     emp.delete()
     return redirect("/emp/emp-view/")
# update function
def update_emp(request,emp_id): 
     emp=Emp.objects.get(pk=emp_id)
     return render(request,"emp/update_emp.html",{
     'emp':emp
     })
    # update handle

def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp_name = request.POST.get("emp-name")
        emp_id_temp= request.POST.get("emp-id")
        emp_age = request.POST.get("emp-age")
        emp_phone_no = request.POST.get("phone-no")  
        emp_address = request.POST.get("emp-address")
        emp_working = request.POST.get("emp-working")
        emp_department = request.POST.get("emp-department")

        e=Emp.objects.get(pk=emp_id)
        e.emp_name = emp_name
        e.emp_id_temp = emp_id
        e.emp_age = emp_age
        e.emp_phone_no = emp_phone_no
        e.emp_address = emp_address
        e.emp_department = emp_department
        e.emp_working = bool(emp_working)  
        
        if emp_working is None:
          e.emp_working=False
        else:
          e.emp_working=True

        e.save()
    return redirect("/emp/emp-view/")

