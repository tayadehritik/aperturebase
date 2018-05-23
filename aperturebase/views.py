from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForM
from django.core.mail import send_mail
from django.contrib import messages

from articles.models import Message


def home(request):
        #return HttpResponse('hey buddy you\'re at home')
        if request.method == "POST":
                form = ContactForM(request.POST)
                if form.is_valid():
                        name = form.cleaned_data['Name']
                        email = form.cleaned_data['sender']
                        
                        subject = form.cleaned_data['subject']
                        message = form.cleaned_data['message']
                        

                        mess = Message()

                        mess.name = name
                        mess.sender = email
                        mess.subject = subject
                        mess.message = message

                        mess.save()
                        
                        messages.success(request,'Message sent')
                        return HttpResponseRedirect('/#message')

        else:
                form = ContactForM()


        return render(request, 'home.html',{'form':form})