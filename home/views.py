from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.views import View
from .models import Register,Destination,Eregister,Addevents,Status
from django.views.generic import ListView,DetailView
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.
class AcceptView(View):
     def get(self, request, pk, *args, **kwargs):
        entry = Eregister.objects.get(pk=pk)
        status= Status(rollno=entry.rollno,eventname=entry.event,status="accepted")
        status.save()
        Eregister.objects.get(pk=pk).delete()
        return render(request,"status.html",{})

class RejectView(View):
     def get(self, request, pk, *args, **kwargs):
        entry = Eregister.objects.get(pk=pk)
        status= Status(rollno=entry.rollno,eventname=entry.event,status="decined")
        status.save()
        Eregister.objects.get(pk=pk).delete()
        return render(request,"regectstatus.html",{})
class EventListView(ListView):
    model=Addevents
    template_name='hom.html'     
    context_object_name='events'
    ordering=['lastdate']

class StorageListView(LoginRequiredMixin,ListView):
    model=Status
    template_name='registeredevents.html'     
    context_object_name='events'
    ordering=['rollno']


class ReqListView(LoginRequiredMixin,ListView):
    model=Eregister
    template_name='reqevents.html'     
    context_object_name='events'
    ordering=['-rollno']

class Reqdetailview(DetailView):
    model=Eregister


# def hom(request):
#     return render(request,'hom.html')
def logout(request):
    return render(request,'logout.html')
def home1(request):
    return render(request,'home1.html')
def login(request):
    if request.method == 'POST':
        rollno=request.POST['rollno']
        password=request.POST['password']
        user=auth.authenticate(username=rollno,password=password)
        if(user is not None):
            auth.login(request,user)
            return redirect('hom')
        else:
            messages.info(request,'invalid username/password')
            return redirect('login')
    else:
        return render(request,'login.html')
            
def register(request):
    if(request.method == 'POST'):
        rolln=request.POST['rollno']
        name=request.POST['name']
        email=request.POST['email']
        year=request.POST['year']
        branch=request.POST['branch']
        section=request.POST['section']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if(password1==password2):
            if(Register.objects.filter(rollno=rolln).exists()):
                messages.info(request,'rollno already exists')
                return redirect('register')
            elif(Register.objects.filter(email=email).exists()):
                messages.info(request,'email exists')
                return redirect('register')
            else:
                user1=Register.objects.create(name=name,rollno=rolln,email=email,year=year,branch=branch,section=section,password=password1)
                user2=User.objects.create_user(username=rolln,password=password1,email=email,first_name=name)
                user1.save()
                user2.save()
                messages.info(request,'successfullly created')
                return redirect('login')

        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')


    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
@login_required
def eregister(request):
    if(request.method == 'POST'):
        rolln=request.POST['rollno']
        email=request.POST['email']
        year=request.POST['year']
        event=request.POST['event']
        branch=request.POST['branch']
        section=request.POST['section']
        grade=request.POST['cgpa']
        backlogs=request.POST['backlogs']
        user=Eregister.objects.create(rollno=rolln,email=email,event=event,grade=grade,backlogs=backlogs,year=year,branch=branch,section=section)
        user.save()
        return redirect('hom')
    else:
        return render(request,'eregister.html')




def addevent(request):
    if(request.method == 'POST'):
       name=request.POST['name']
       lastdate=request.POST['lastdate']
       eventdate=request.POST['eventdate']
       user=Addevents.objects.create(name=name,lastdate=lastdate,eventdate=eventdate)
       user.save()
       return redirect('hom')
    else:
        return render(request,'addevent.html')


def registeredevents(request):
    ereg=Eregister.objects.filter(rollno=request.user)
    return render(request,'registeredevents.html',{'ereg':ereg[0]})


@login_required
def profile(request):
    register = Register.objects.filter(rollno=request.user)
    return render(request,'profile.html',{'register':register[0]})