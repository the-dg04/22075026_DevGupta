from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UrlMap
from .forms import UrlForm
from .urlfuncs import *
from django.conf import settings

def display_url(request,short_url):
    return HttpResponse(f"<div>Successfully generated smol url:<br/>{settings.BASE_URL+'/urls/'+short_url}</div><br><a href=\"/\">go home</a>")

def newPath(request):
    if request.method=="POST":
        form=UrlForm(request.POST)
        if(form.is_valid()):
            new_url=form.save(commit=False)
            new_short_url=generate_url()
            new_url.short_url=new_short_url
            new_url.save()
            return redirect(f"/display/{new_short_url}")

    form=UrlForm()
    return render(request,"newPath.html",{'form':form})

def pathList(request):
    m=list(UrlMap.objects.all())
    return render(request,"pathList.html",{"url_list":m})


def redirectTo(request,short_url):
    try:
        m=UrlMap.objects.get(short_url=short_url)
        return redirect(m.long_url)
    except:
        return HttpResponse("No such smol url found")
        
