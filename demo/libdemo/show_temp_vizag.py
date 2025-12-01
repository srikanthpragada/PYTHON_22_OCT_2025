
import requests

# lat = 17.6974
# longt = 83.2990
lat = 47.6061
longt = 122.3328

resp = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={longt}&current=temperature_2m")
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit(1)

details = resp.json()

weather = details['current']
temp = weather["temperature_2m"]
timezone = details['timezone']
print(f"Temp is at {timezone} timezone is : {temp} C")



