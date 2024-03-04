from django.urls import path

from doctorclinicbooking_app import views


urlpatterns = [
    path('',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('logincode',views.logincode,name="logincode"),
    path('adminindex',views.adminindex,name="adminindex"),
    path('add_awareness',views.add_awareness,name="add_awareness"),
    path('doc_verification',views.doc_verification,name="doc_verification"),
    path('manage_awareness',views.manage_awareness,name="manage_awareness"),
]