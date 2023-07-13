import requests
import json
import re

def normalize_mac_address(input_string):
    mac_address_pattern = r'^([0-9A-Fa-f]{2})[:-]?([0-9A-Fa-f]{2})[:-]?([0-9A-Fa-f]{2})[:-]?([0-9A-Fa-f]{2})[:-]?([0-9A-Fa-f]{2})[:-]?([0-9A-Fa-f]{2})$'
    match = re.match(mac_address_pattern, input_string)
    if match:
        normalized = ':'.join(match.groups())
        return normalized.upper()
    else:
        return None

mac_addresses = []


while 1 == 1:
    input1 = input("Enter Mac Address/BSSID One at a time, type RUN to run the program:")
    if input1 == "RUN":
        break
    elif normalize_mac_address(input1) == None:
        print("Mac Address format invalid, retype or type RUN to run the program:")
    else:
       mac_addresses.append(normalize_mac_address(input1))
# API endpoint and your API key
url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=YOUR_API_KEY

# MAC addresses or BSSIDs for which you want to find the location

# Construct the request payload
payload = {'wifiAccessPoints': [{'macAddress': mac} for mac in mac_addresses]}

# Send the request
response = requests.post(url, data=json.dumps(payload))

# Parse the response
if response.status_code == 200:
    result = response.json()
    print('Location found:')
    print('Latitude:', result['location']['lat'])
    print('Longitude:', result['location']['lng'])
    print('https://www.latlong.net/c/?lat='+ str(result['location']['lat']) + '&long='+ str(result['location']['lng']))

else:
    print('Error:', response.status_code)
    print(response.text)
