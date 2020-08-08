#!/usr/bin/env python3

# API refrence: https://bungie-net.github.io/multi/operation_get_Destiny2-GetProfile.html#operation_get_Destiny2-GetProfile
# learn more at https://github.com/patclarke/LearningDestiny2APIPython3

# import libraries
import requests

# static variables
# add your own API key here 
HEADERS = {"X-API-Key":'YOUR_API_KEY_HERE'}

# dynamic variables
# Path: /Destiny2/{membershipType}/Profile/{destinyMembershipId}/
# membershipType is defined here https://bungie-net.github.io/multi/schema_BungieMembershipType.html#schema_BungieMembershipType
# for this example we are using membnershipType 3 for Steam
# membershipID is defined as "Destiny membership ID." sorry thats sucks but we found the ID in script 02_SearchDestinyPlayer_example.py
# the last part of this URL is the ComponentType. Find out more at https://bungie-net.github.io/multi/schema_Destiny-DestinyComponentType.html
# for this example we are ussing components 205 "CharacterEquipment" to get a list of equiped items
r = requests.get("https://www.bungie.net/Platform/Destiny2/3/Profile/4611686018467446894/?components=205", headers=HEADERS);

response = r.json()
print(response)
