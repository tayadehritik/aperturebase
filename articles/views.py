from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles
# Create your views here.
def article_list(request):
    article = Articles.objects.all().order_by('date')
    return render(request, 'articles/article_list.html',{'article':article})

def article_detail(request,slug):
    art1 = Articles.objects.get(slug=slug)
    body = art1.body
    
    di = ['img0','img1','img2','img3','img4','img5','img6','img7','img8','img9']

    
    for i in di:

        a = body.find('!! '+i+" !!")
        #exec('art1.'+body[a+3:a+8]+'.url')
        if(a!=-1):

            b = getattr(art1,i).url

            body = body[:a] + "<img src=" + "'" +b+"'"+" class='img-responsive ' style='margin: 0 auto;width:100%; border: 5px solid;'/>"+body[a+10:len(body)]
        else:
            pass
    return render(request, 'articles/article_detail.html',{'art1':art1,'final':body})