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
    path('chatwithdr', views.chatwithdr, name='chatwithdr'),
    path('coun_msg_user/<int:id>', views.coun_msg_user, name='coun_msg_user'),
    path('chatview', views.chatview, name='chatview'),
    path('coun_msg/<int:id>', views.coun_msg, name='coun_msg'),
    path('coun_insert_chat/<str:msg>/<int:id>', views.coun_insert_chat, name='coun_insert_chat'),
]