from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_details, name="employees_detail"),
    path('<int:emp_id>/', views.employee_info, name="employee_info"),
    path('add/', views.add_employee, name="add_employee"),
    path('<int:emp_id>/delete/', views.employee_delete , name = 'employee_delete'),
    path('<int:emp_id>/edit/', views.edit_employee, name="edit_employee"),

    

]
