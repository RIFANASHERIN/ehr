import datetime
import json
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
from doctorclinicbooking_app.models import *
def login(request):
    return render(request,"loginindex.html")

def logout(request):
    auth.logout(request)
    return render(request,"loginindex.html")


def logincode(request):
    uname = request.POST['uname']
    password=request.POST['pwrd']
    try:
        ob=Login.objects.get(username=uname,password=password)

        if ob.type=="admin":
            ob1 = auth.authenticate(username="admin", password="123")
            if ob is not None:
                auth.login(request, ob1)
            request.session['lid']=ob.id
            return HttpResponse('''<script>alert("successfully login");window.location="/adminindex"</script>''')
        elif ob.type=="Doctor":
            ob1 = auth.authenticate(username="admin", password="123")
            if ob is not None:
                auth.login(request, ob1)
            request.session['lid'] = ob.id
            return HttpResponse('''<script>alert("successfully login");
            window.location="/Dr_home"</script>''')
        else:
            return HttpResponse('''<script>alert("invalid");
                window.location="/"</script>''')

    except:
        return HttpResponse('''<script>alert("invalid");
                        window.location="/"</script>''')


@login_required(login_url='/')
def adminindex(request):
    return render(request,"ADMIN/adminindex.html")

def regindex (request):
    return render(request,"regindex.html")

def Doctor_registration(request):
    return render(request,"registerindex.html")

def Dr_home(request):
    return render(request,"DOCTOR/drindex.html")

