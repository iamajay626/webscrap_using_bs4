from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

from webscarpapp.models import links


# Create your views here.
def home(request):
    if request.method=="POST":
        link_new=request.POST.get('page','')
        urls=requests.get(link_new)
        beautisoup=BeautifulSoup(urls.text,'html.parser')

        for link in beautisoup.find_all('a'):
            li_address=link.get('href')
            li_name=link.string
            links.objects.create(address=li_address,string_name=li_name)
        return HttpResponseRedirect('/')
    else:
        data_value=links.objects.all()


    return render(request,'home.html',{'data_value':data_value})