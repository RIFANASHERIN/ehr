from django.urls import path

from doctorclinicbooking_app import views

urlpatterns = [
    path('',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('logincode',views.logincode,name="logincode"),
    path('adminindex',views.adminindex,name="adminindex"),
     path('Doctor_registration', views.Doctor_registration, name="Doctor_registration"),
    path('Dr_home',views.Dr_home, name="Dr_home"),
]