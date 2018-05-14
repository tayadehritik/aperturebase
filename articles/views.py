from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles
# Create your views here.
def article_list(request):
    article = Articles.objects.all().order_by('date')
    return render(request, 'articles/article_list.html',{'article':article})

def article_detail(request,slug):
    art1 = Articles.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html',{'art1':art1})