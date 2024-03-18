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

@login_required(login_url='/')
def add_awareness(request):
    return render(request,"ADMIN/Add_awareness.html")

@login_required(login_url='/')
def add_awarenesscode(request):
    aw=request.POST['textfield']
    det=request.POST['textfield2']
    ved=request.FILES['file']
    fs=FileSystemStorage()
    fn=fs.save(ved.name,ved)
    ob=Awareness()
    ob.video=fn
    ob.Awarenes=aw
    ob.Details=det
    ob.Date=datetime.datetime.today()
    ob.save()
    return HttpResponse('''<script>alert("Awareness Added"); window.location="/manage_awareness#about"</script>''')


@login_required(login_url='/')
def delete_awareness(request,id):
    ob=Awareness.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Awareness Deleted"); window.location="/manage_awareness#about"</script>''')



def regindex (request):
    return render(request,"regindex.html")

def Doctor_registration(request):
    return render(request,"registerindex.html")

def Dr_home(request):
    return render(request,"DOCTOR/drindex.html")

@login_required(login_url='/')
def doc_verification(request):
    ob=Doctor.objects.all()
    return render(request,"ADMIN/dr_verification.html",{'val':ob})

@login_required(login_url='/')
def doc_verificationsearch(request):
    dep=request.POST['name']
    ob=Doctor.objects.filter(Department__icontains=dep)
    return render(request,"ADMIN/dr_verification.html",{'val':ob})

def chatwithdr(request):
    ob = Doctor.objects.all()
    return render(request,"ADMIN/chat with dr.html",{'val':ob})




def chatview(request):
    ob = Doctor.objects.all()
    d=[]
    for i in ob:
        r={"name":i.Firstname + i.Lastname,'photo':i.photo.url,'email':i.Email,'loginid':i.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)




def coun_insert_chat(request,msg,id):
    print("===",msg,id)
    ob=Chat()
    ob.Fromid=Login.objects.get(id=request.session['lid'])
    ob.Toid=Login.objects.get(id=id)
    ob.Message=msg
    ob.Date=datetime.datetime.now().strftime("%Y-%m-%d")
    ob.Time=datetime.datetime.now()
    ob.save()

    return JsonResponse({"task":"ok"})
    # refresh messages chatlist



def coun_msg(request,id):

    ob1=Chat.objects.filter(Fromid__id=id,Toid__id=request.session['lid'])
    ob2=Chat.objects.filter(Fromid__id=request.session['lid'],Toid__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.Fromid.id,"msg":i.Message,"date":str(i.Date)+" "+str(i.Time).split(".")[0],"chat_id":i.id})

    obu=Doctor.objects.get(LOGIN__id=id)


    return JsonResponse({"data":res,"name":obu.Firstname + obu.Lastname,"photo":obu.photo.url,"user_lid":obu.LOGIN.id})


def coun_msg_user(request,id):

    ob1=Chat.objects.filter(Fromid__id=id,Toid__id=request.session['lid'])
    ob2=Chat.objects.filter(Fromid__id=request.session['lid'],Toid__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.Fromid.id,"msg":i.Message,"date":str(i.Date)+" "+str(i.Time).split(".")[0],"chat_id":i.id})

    obu=User.objects.get(LOGIN__id=id)


    return JsonResponse({"data":res,"name":obu.Firstname +" "+ obu.Lastname,"photo":obu.photo.url,"user_lid":obu.LOGIN.id})


