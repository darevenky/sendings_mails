from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from app.forms import *
from django.core.mail import send_mail


def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo, 'pfo':pfo}

    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)

        if ufd.is_valid() and pfd.is_valid():
            usuo=ufd.save(commit=False)
            #password=ufd.cleaned_data['password']
            usuo.set_password(ufd.cleaned_data['password'])
            usuo.save()
            #usuo=un saved user object

            uspo=pfd.save(commit=False)
            uspo.username=usuo
            uspo.save()
            #uspo=un saved profile object

            send_mail('registration',
                      'Registration is completed succefully',
                      'darevenky96@gmail.com',
                      [usuo.email],
                      fail_silently=False
                      )

            return HttpResponse('Registration is successfullll')
        else:
            return HttpResponse('data is not valid')
    return render(request,'registration.html',d)