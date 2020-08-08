#!/usr/bin/env python3

# API refrence: https://bungie-net.github.io/#Destiny2.SearchDestinyPlayer
# learn more at https://github.com/patclarke/LearningDestiny2APIPython3

# import libraries
import requests

# static variables
# add your own API key here 
HEADERS = {"X-API-Key":'YOUR_API_KEY_HERE'}

# dynamic variables
# Path: /Destiny2/SearchDestinyPlayer/{membershipType}/{displayName}/
# membershipType is defined here https://bungie-net.github.io/multi/schema_BungieMembershipType.html#schema_BungieMembershipType
# for this example we are using membnershipType 3 for Steam
# displayName is defined as "The full gamertag or PSN id of the player. Spaces and case are ignored."
# for this example we are using the Steam display name TroyjanMan
r = requests.get("https://www.bungie.net/Platform/Destiny2/SearchDestinyPlayer/3/TroyjanMan/", headers=HEADERS);

response = r.json()
print(response)
