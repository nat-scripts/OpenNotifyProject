# All parts combined to loop until '4' is pressed

import requests

def loc():
	loc = requests.get('http://api.open-notify.org/iss-now')
	loc_json = loc.json()
	print("\nCurrent Latitude of ISS :",loc_json['iss_position']['latitude'])
	print("Current Longitude of ISS :",loc_json['iss_position']['longitude'],"\n")
	
def iss_pass():
	loc = {}
	loc['lat'] = int(input("\nLatitude: "))
	loc['lon'] = int(input("Longitude: "))
	iss_pass = requests.get('http://api.open-notify.org/iss-pass.json', params=loc)
	iss_pass_json = iss_pass.json()

	print("passes :", iss_pass_json['request']['passes'])
	for var in iss_pass_json['response']:
		print("duration:", var['duration'], "risetime:", var['risetime'])	
	print("\n")

def people():
	people = requests.get('http://api.open-notify.org/astros')
	people_json = people.json()
	print("\nThe number of people in space : ",people_json['number'])
	
	for p in people_json['people']:
		print(p['name'])
	print("\n")

def match():	
	if choice == 1:
		loc()
	elif choice == 2:
		iss_pass()
	elif choice == 3:
		people()
	elif choice == 4:
		print("Exiting...")
		exit()
	else:
		print("\nInvalid Choice\n")

choice = 0
while choice != 4:
	choice = int(input("Press\n1 - Current Location of ISS\n2 - Overhead Pass Prediction of ISS\n3 - Number of People in Space\n4 - Exit\n"))
	match()


		


