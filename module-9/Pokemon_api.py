#Juedeja Richard - Module9.2 - 5/4/25
#Test the connection to your API, output results.
#Print out the response from the request, with no formatting.
#Print out the response with same formatting as the tutorial program.

import requests
response = requests.get("https://pokeapi.co/api/v2/item-category/?limit=3")
print(response.status_code)
print(response.json())
#imported requests library and make GET request to Pokemon api
#limit response results to 5

import json

def poke_print(obj):
    text = json.dumps(obj, sort_keys= True, indent=4)
    print(text)
#import json package and create formating for response in function

#call the poke print function
poke_print(response.json())