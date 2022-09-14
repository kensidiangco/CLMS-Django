from django.urls import path
from . import views

urlpatterns = [
    path('forms/', views.formPage, name="formPage"),
    path('register/', views.registerPage, name="registerPage"),
    path('ITDept/register/', views.ITDeptAccountRegister, name="ITDeptAccountRegister"),

    path('admin/dashboard/', views.adminDashboard, name="adminDashboard"),
    path('ITDept/dashboard/', views.ITDeptDashboard, name="ITDeptDashboard"),
    path('profile/', views.profile, name="profile"),
    path('theme', views.theme, name="theme"),
    
]