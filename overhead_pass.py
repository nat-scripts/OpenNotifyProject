#Basic script to get the overhead pass details of ISS

import requests

loc = {}
loc['lat'] = int(input("Latitude: "))
loc['lon'] = int(input("Longitude: "))

iss_pass = requests.get('http://api.open-notify.org/iss-pass.json', params=loc)

iss_pass_json = iss_pass.json()

print("passes :", iss_pass_json['request']['passes'])
for var in iss_pass_json['response']:
	print("duration:", var['duration'], "risetime:", var['risetime'])	




