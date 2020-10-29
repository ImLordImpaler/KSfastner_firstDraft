from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login , logout
from django.http import JsonResponse
from .forms import CallBackForm

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


    

def callBack(request):
    form = CallBackForm()
    params ={
        'form' : form
    }
    return render(request , 'basic/new/callBack.html' , params)

    