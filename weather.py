import requests, sys, bs4, webbrowser
from uszipcode import SearchEngine

if len(sys.argv) > 1:
    # get zip code from command line
    zip_code = ''.join(sys.argv[1:])
    
    # us uszipcode database module to find that zip code's
    # latitude and longitude coordinates
    search = SearchEngine(simple_zipcode=True)
    zipcode = search.by_zipcode(zip_code)
    zips_dict = zipcode.to_dict()
    lng = zips_dict['lng']
    lat = zips_dict['lat']
    
    # open the weather page to the right area (in case you want more detailed weather info)
    webbrowser.open("https://forecast.weather.gov/MapClick.php?lat=%s&lon=%s" % (lat, lng))

    # also save the html of the page to a file and get the current weather from it
    res = requests.get("https://forecast.weather.gov/MapClick.php?lat=%s&lon=%s" % (lat, lng))
    res.raise_for_status()
    currentWeather = bs4.BeautifulSoup(res.text, features="html.parser")
    weather_html = currentWeather.select(".myforecast-current-lrg")
    weather = weather_html[0].getText()
 
    print(weather)
 
