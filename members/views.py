from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import RegisterForm
from mybandblog.models import Member

def register(request):
    if request.method == 'GET':
        form  = RegisterForm()
        context = {'form': form}
        return render(request, 'authenticate/register.html', context)
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            user = form.cleaned_data.get('username')
            return render(request, 'authenticate/user.html')
            
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'authenticate/register.html', context)

    return render(request, 'authenticate/register.html', {})

def userhome(request):
    members = Member.objects.all()
    return render(request,'authenticate/user.html',{'name':members})

def userpage(request):
    return render(request,'authenticate/user.html',{})
