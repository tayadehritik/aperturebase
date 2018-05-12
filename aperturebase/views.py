from django.http import HttpResponse
from django.shortcuts import render


def home(request):
        #return HttpResponse('hey buddy you\'re at home')
        return render(request, 'home.html')