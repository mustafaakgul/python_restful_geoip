from django.shortcuts import render
import requests

# Caching improves performance so in this case we are not changing location soo much
def index(request):
    # Boolean Value
    is_cached = ('geodata' in request.session)

    if not is_cached:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
        response = requests.get('http://api.ipstack.com/46.221.10.202?access_key=4b093161c03e1ece4286ecfb3cfbc5af')
        request.session['geodata'] = response.json()

    geodata = request.session['geodata']

    context = {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': 'AIzaSyC1UpCQp9zHokhNOBK07AvZTiO09icwD8I',
        'is_cached': is_cached
    }

    return render(request,
                  'core/index.html',
                  context)

"""
First Version 
def home(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('http://freegeoip.net/json/%s' % ip_address)
    geodata = response.json()
    return render(request, 'core/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': 'AIzaSyC1UpCQp9zHokhNOBK07AvZTiO09icwD8I'  # Don't do this! This is just an example. Secure your keys properly.
    })
"""