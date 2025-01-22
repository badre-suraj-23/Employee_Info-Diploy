from django.contrib import admin
from.models import Emp

@admin.register(Emp)
class EmpAdmin(admin.ModelAdmin):
    list_display = ['emp_name','emp_id','emp_age','emp_phone_no','emp_address','emp_department','emp_working']
    search_fields =['emp_name','emp_phone_no','emp_department']
    list_per_page = 5

               
               

