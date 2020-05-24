#Basic script to get the current location of ISS

import requests

loc = requests.get('http://api.open-notify.org/iss-now')

loc_json = loc.json()

print("Current Latitude of ISS :",loc_json['iss_position']['latitude'])
print("Current Longitude of ISS :",loc_json['iss_position']['longitude'])
	
