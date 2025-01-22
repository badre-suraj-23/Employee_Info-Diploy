from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    # path("home/",emp_home),
    path("add-emp/",add_emp),
    path("emp-view/",emp_view),
    path("follow/",follow),
    path("delete-emp/<int:emp_id>",delete_emp),
    path("update-emp/<int:emp_id>",update_emp),
    path("do-update-emp/<int:emp_id>",do_update_emp),
    
]