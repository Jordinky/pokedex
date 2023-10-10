import requests

url = 'https://pokeapi.co/api/v2/pokemon/6/'
headers = {'Content-Type': 'text/html'}
request = requests.get(url,headers)
print(f"status code: {request.status_code}")

response = request.json()

print(response.keys())
print(f"id: {response['id']}" )
print(f"name: {response['name']}" )
print(f"stats: {response['stats']}" )
print(f"type: {response['types']}" )
print(f"weight: {response['weight']}" )
