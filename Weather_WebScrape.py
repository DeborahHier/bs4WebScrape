import requests, sys, bs4
from uszipcode import SearchEngine

# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# type(res)
# res.status_code == requests.codes.ok
# len(res.text)
# print(res.text[:250])


# res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
# try:
#    res.raise_for_status()
# except Exception as exc:
#    print("There was a problem: " + str(exc))

# res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
# res.raise_for_status()
# playFile = open("RomeoAndJuliet.txt", "wb")
# for chunk in res.iter_content(100000):
#    playFile.write(chunk)

# playFile.close()



# res = requests.get("https://nostarch.com")
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text)
# type(noStarchSoup)


# <p class="myforecast-current-lrg">28°F</p>

if len(sys.argv) > 1:
    # get zip code from command line
    zip_code = ''.join(sys.argv[1:])

print(zip_code)

 #   search = SearchEngine(simple_zipcode=True)
#    zipcode = search.by_zipcode(zip_code)
#    zipcode.to_dict()
#    lng = zipcode['lng']
#    lat = zipcode['lat']
    
#    webbrowser.open("https://forecast.weather.gov/MapClick.php?lat=%s&lon=%s" % (lat, lng))
                    
    
