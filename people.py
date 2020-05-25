import requests

people = requests.get('http://api.open-notify.org/astros')

people_json = people.json()

print("The number of people in space : ",people_json['number'])

for p in people_json['people']:
	print(p['name'])

