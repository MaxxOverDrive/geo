from django.shortcuts import render
from ip2geotools.databases.noncommercial import DbIpCity




# Create your views here.
def index(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    response = DbIpCity.get('72.234.149.8', api_key='free')

    #GOOGLE MAPS

    

    return render(request, 'index.html', {'ip': ip, 'response': response})
    