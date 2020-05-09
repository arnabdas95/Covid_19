from django.shortcuts import render, redirect
import requests
import json

from django.urls import reverse

url = 'https://api.covid19india.org/state_district_wise.json'
page = requests.get(url)
data = page.json()
state ='West Bengal'
area ='Kolkata'
def home(request):
        global data,state,area
        if request.method == 'POST'  and 'statename' in request.POST:
                state = request.POST.get("st")
        return render(request, 'home.html', {'data': data})



def details(request):
        global state
        if request.method == 'POST' and 'statename' in request.POST:
                state = request.POST.get("st")

        area = request.POST.get("area")
        district = data[state]['districtData']

        return render(request,'details.html',{'state':state,'area':area,'district': district})