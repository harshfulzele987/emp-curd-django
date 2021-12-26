from django.contrib import admin
from django.urls import path ,include
from . import views
urlpatterns = [
    
    path('list/' , views.employee_list),
    path('form/' , views.employee_form)

]
