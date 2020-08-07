#!/usr/bin/env python3

# example was pulled from 
# http://destinydevs.github.io/BungieNetPlatform/docs/Getting-Started
# learn more at https://github.com/patclarke/LearningDestiny2APIPython3

# import libraries
import requests

# static variables
# add your own API key here 
HEADERS = {"X-API-Key":'YOUR_API_KEY_HERE'}

# dynamic variables
r = requests.get("https://www.bungie.net/platform/Destiny/Manifest/InventoryItem/1274330687/", headers=HEADERS);

#convert the json object we received into a Python dictionary object
#and print the name of the item
inventoryItem = r.json()
print(inventoryItem['Response']['data']['inventoryItem']['itemName'])
