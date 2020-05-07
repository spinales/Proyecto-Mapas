import requests
import json

overpass_url = "http://overpass-api.de/api/interpreter"
overpass_query = """
[out:json];
area["ISO3166-1"="DO"][admin_level=2];
(
 way["hotel"](area);
);
out center;
"""
response = requests.get(overpass_url, 
                        params={'data': overpass_query})
data = response.json()
print(data)
# with open('data.json','w') as file:
#     json.dump(data, file, indent=4)