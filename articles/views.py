from django.shortcuts import render
from .models import Articles
# Create your views here.
def article_list(request):
    article = Articles.objects.all().order_by('date')
    return render(request, 'articles/article_list.html',{'article':article})