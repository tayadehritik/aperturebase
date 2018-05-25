from django.shortcuts import render
from articles.models import Cat
# Create your views here.
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages


def cat(request, CatHead):
    cat = Cat.objects.get(CatHead=CatHead)
    labels = ['im0','im1','im2','im3','im4','im5','im6','im7','im8','im9']
    c = list()
    for i in labels:
        b = getattr(cat,i).url
        c.append(b)
    
    return render(request, 'cats/cats.html',{'cat':cat,'c':c})