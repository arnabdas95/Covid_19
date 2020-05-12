from django.contrib import messages
from django.shortcuts import render, redirect
import requests

url = 'https://api.covid19india.org/state_district_wise.json'
country_url ='https://api.covid19api.com/summary'

country_page= requests.get(country_url)
page = requests.get(url)

data = page.json()
world_data = country_page.json()

worldtc=world_data['Global']['TotalConfirmed']
worldtd=world_data['Global']['TotalDeaths']
worldtr=world_data['Global']['TotalRecovered']
world = {'worldtc':worldtc,'worldtd':worldtd,'worldtr':worldtr}

chainatc = world_data['Countries'][35]['TotalConfirmed']
chainatd  =  world_data['Countries'][35]['TotalDeaths']
chainatr =  world_data['Countries'][35]['TotalRecovered']
chaina = {'chainatc':chainatc,'chainatd':chainatd,'chainatr':chainatr}

francetc = world_data['Countries'][59]['TotalConfirmed']
francetd  =  world_data['Countries'][59]['TotalDeaths']
francetr =  world_data['Countries'][59]['TotalRecovered']
france = {'francetc':francetc,'francetd':francetd,'francetr':francetr}

indiatc = world_data['Countries'][76]['TotalConfirmed']
indiatd  =  world_data['Countries'][76]['TotalDeaths']
indiatr =  world_data['Countries'][76]['TotalRecovered']
india = {'indiatc':indiatc,'indiatd':indiatd,'indiatr':indiatr}

uktc = world_data['Countries'][175]['TotalConfirmed']
uktd  =  world_data['Countries'][175]['TotalDeaths']
uktr =  world_data['Countries'][175]['TotalRecovered']
uk = {'uktc':uktc,'uktd':uktd,'uktr':uktr}

usatc = world_data['Countries'][176]['TotalConfirmed']
usatd  =  world_data['Countries'][176]['TotalDeaths']
usatr =  world_data['Countries'][176]['TotalRecovered']
usa = {'usatc':usatc,'usatd':usatd,'usatr':usatr}




state = area = ''
confirmed = active = deceased = recovered = ''
val = 0


def home(request):
    global world,india, chaina ,uk,usa,france
    return render(request, 'home.html', {'data': data,'world': world,'india':india,'usa':usa,'uk':uk,'france':france,'chaina':chaina})


def details(request):
    global state, confirmed, area, val, active, recovered, deceased,data

    if request.method == 'POST' and 'state_name' in request.POST:
        state = request.POST.get("st")
    if state == '':
        messages.success(request, 'Cannot Fetch data from server!Try again')
        return redirect('/')

    district = data[state]['districtData']

    if request.method == 'POST' and 'area_name' in request.POST:
        try:
            area = request.POST.get("area")
            confirmed = district[area]['confirmed']
            active = district[area]['active']
            deceased = district[area]['deceased']
            recovered = district[area]['recovered']
            val = 1
        except:
            messages.success(request, 'Cannot Fetch data from server! Try again.')
            return redirect('/')

    else:
        val = 0
    print("hello")


    return render(request, 'details.html',
                  {'state': state, 'area': area, 'district': district, 'confirmed': confirmed, 'active': active,
                   'deceased': deceased, 'recovered': recovered, 'val': val})
