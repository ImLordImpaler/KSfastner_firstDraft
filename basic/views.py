from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login , logout
from django.http import JsonResponse
from .forms import CallBackForm
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

import json
# Create your views here.
def homepage(request):
    
    return render(request , 'basic/new/action.html' )




def logoutPage(request):
    pass

def loginPage(request):

    if request.method =='POST':
        email = request.POST.get('emailId')
        passwd  = request.POST.get('passwd')
        user = authenticate(request , username=email , password = passwd)

        if user is not None:
            login(request , user)
            return redirect('home')
    return render(request , 'basic/login.html')


    
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def callBack(request):
    if request.method == 'POST':
        email = request.POST.get('emailId' , '')
        name = request.POST.get('nameId' , '')
        phone = request.POST.get('phoneId' , '')
        subject = 'Call Back info:'
        body = 'Welcome to KSFastners'+email + '.' + name + '.' + phone + '.'
        if email and name and phone :
            email = EmailMessage(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                ['1803010164@ipec.org.in']
            )
            email.fail_silently = False
            email.send()
            return redirect('home')
        else :
            return HttpResponse('<h3> Wrong Credentials </h3>')
    else : 
        return render(request , 'basic/callBack.html')
    

    
  
    return render(request , 'basic/callBack.html')

    