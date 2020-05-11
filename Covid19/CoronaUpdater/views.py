from django.contrib import messages
from django.shortcuts import render, redirect
import requests

url = 'https://api.covid19india.org/state_district_wise.json'
page = requests.get(url)
data = page.json()
state = area = ''
confirmed = active = deceased = recovered = ''
val = 0


def home(request):

    return render(request, 'home.html', {'data': data})


def details(request):
    global state, confirmed, area, val, active, recovered, deceased,data

    if request.method == 'POST' and 'state_name' in request.POST:
        state = request.POST.get("st")
    if state == '':
        messages.success(request, 'Cannot Fetch data! Please Try again')
        return redirect('/')

    district = data[state]['districtData']

    if request.method == 'POST' and 'area_name' in request.POST:
        area = request.POST.get("area")
        confirmed = district[area]['confirmed']
        active = district[area]['active']
        deceased = district[area]['deceased']
        recovered = district[area]['recovered']
        if area == 'none' or confirmed == 'none' or active == 'none' or deceased == 'none' or recovered == 'none':
            messages.success(request, 'Cannot Fetch data! Try again.')
            print(confirmed)
            return redirect('/')
        val = 1
    else:
        val = 0



    return render(request, 'details.html',
                  {'state': state, 'area': area, 'district': district, 'confirmed': confirmed, 'active': active,
                   'deceased': deceased, 'recovered': recovered, 'val': val})
