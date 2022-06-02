from django.shortcuts import render,redirect 
from django.http import HttpResponse
from .models import Registration
from .models import Job
from .models import Candidate
from .models import HrReg
from .models import Jobinfo

from django.views import View
def job(request):
    if (request.session.has_key("uid")):
        suid=request.session["uid"]
        data1 = Job.objects.all()

        return render(request,"jobportal/job.html",{"res":"data inserted succesfully","d":data1})
    else:
        return redirect("login")
    
def candidate(request):
    if (request.session.has_key('uid')):
        suid=request.session['uid']
        job = Job.objects.all()
        if request.method=="POST":
            s = Candidate(email =request.POST["txtemail"],jobid=request.POST["ddljob"],applydate=request.POST["applydate"],
            cname=request.POST["txtcandidate"])
            s.save()
            return render(request,"jobportal/candidate.html",{"res":job,"msg":"data inserted successsfully"})
        return render(request,"jobportal/candidate.html",{"res":job,"jid":(request.GET["q"])})    

def registration(request):
    Qulification=["10th","12th","diploma","graduation","post graduation"]
    if request.method=="POST":
        r = Registration(email=request.POST["email"],password=request.POST["password"],
        mobileno =request.POST["mobileno"],technology=request.POST["technology"],
        candidatetype=request.POST["candidatetype"],higherquli=request.POST["education"])
        r.save()
        return render(request,"jobportal/registration.html",{"data": Qulification,"data1":"registration successsfully"})
    return render(request,"jobportal/registration.html",{"data":Qulification})

def clogin(request):
    if request.method=="POST":
        r = Registration.objects.filter(email=request.POST["email"],password=request.POST["password"])
        if r.count()>0:
            request.session['uid']=request.POST["email"]
            if request.POST["chk"]:
                res= HttpResponse(status=302)
                res.set_cookie('ukey',request.POST["email"])
                res.set_cookie('upass',request.POST["password"])
                res['Location'] ='job'
                return res
            else:
                return render(request,"plus/clogin.html",{"res":"invalid user id password"})
    else:
        c1=""
        c2=""
        if request.COOKIES.get('ukey'):
          c1=request.COOKIES["ukey"]
          c2=request.COOKIES["upass"]
    return render(request,"jobportal/clogin.html",{"email":c1,"password":c2})

def logout(request):
   res = HttpResponse(status=302)
   res.delete_cookie('ukey',"/")
   res.delete_cookie('upass',"/")
   del request.session["uid"]
   res['Location']='login'
   return res 

def home(request): 
    return render(request,"jobportal/home.html")

def hlogin(request):
    if request.method=="POST":
        r = Registration.objects.filter(email=request.POST["email"],password=request.POST["password"])
        if r.count()>0:
            request.session['uid']=request.POST["email"]
            if request.POST["chk"]:
                res= HttpResponse(status=302)
                res.set_cookie('ukey',request.POST["email"])
                res.set_cookie('upass',request.POST["password"])
                res['Location'] ='jobcreate'
                return res
            else:
                return render(request,"jobportal/hlogin.html",{"res":"invalid user id password"})
    else:
        c1=""
        c2=""
        if request.COOKIES.get('ukey'):
          c1=request.COOKIES["ukey"]
          c2=request.COOKIES["upass"]
    return render(request,"jobportal/hlogin.html",{"email":c1,"password":c2})


def hrreg(request):
    
    if request.method=="POST":
        r = HrReg(email=request.POST["email"],password=request.POST["password"],
        mobileno =request.POST["mobileno"],companyname=request.POST["companyname"])
        r.save()
        return render(request,"jobportal/hrreg.html",{"data1":"registration successsfully"})
    return render(request,"jobportal/hrreg.html")

def jobinfo(request):
    
    if request.method=="POST":
        r = Jobinfo(jobtitle=request.POST["title"],experience=request.POST["experience"],
       jobdescription =request.POST["description"],uploadimage=request.POST["image"],
       technology=request.POST["technology"],postdate=request.POST["postdate"],
       duedate =request.POST["duedate"])
        r.save()
        return render(request,"jobportal/job.html",{"res":Jobinfo.objects.all()})
    return render(request,"jobportal/jobinfo.html",{"res":Jobinfo.objects.all()})


# Create your views here.
