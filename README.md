# LearningDestiny2APIPython3
Learning how to use Destiny 2 API with Python3

# Getting Srtarted
## Helpful Resources 
* http://destinydevs.github.io/BungieNetPlatform/docs/Getting-Started
* http://destinydevs.github.io/BungieNetPlatform/docs/Manifest
* https://bungie-net.github.io/
* https://bungie-net.github.io/multi/schema_Destiny-DestinyComponentType.html

## Before You Begin
The first thing you will need to do is get an API key from bungie. This key will be used in all of our test scripts. Think of it like a password that allows you to use the Destiny API. You get your API key from: 
https://www.bungie.net/en/Application
NOTE: If you have not signed into bungie.net do that first or this link will not redirect you to the right place


## First Python Script
Copy this script
https://github.com/patclarke/LearningDestiny2APIPython3/blob/master/examples/01_gjallarhorn_example.py

On line 12 we will edit the section that says YOUR_API_KEY_HERE. Replace that text with the key you recived in the step above. For now on we will skip mentioning this step but it will be required on all scripts downloaded from this repo.

Now run the script and you should see 
"Gjallarhorn"

Congradulations you have made your first Python API call.

## Second Python Script
Copy this script 
https://github.com/patclarke/LearningDestiny2APIPython3/blob/master/examples/02_SearchDestinyPlayer_example

Whith this script we are obtaining the users "destinyMembershipId". We will use the destinyMembershipId to be able to pull more details about the users charactors.

## Third Python Script
Copy this script 
https://github.com/patclarke/LearningDestiny2APIPython3/blob/master/examples/03_GetProfile_example.py

With this script we are obtaining the users "CharacterEquipment". We will need to decoded the response as all gear will be hashed.


