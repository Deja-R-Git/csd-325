#Juedeja Richard - Module9.2 - 5/4/25
#making api request in python following tutorial

import requests
#import requests library
response = requests.get("http://api.open-notify.org/astros.json")
#make a GET request to the API and print Status code
print(response.status_code)

#import jason package
import json
#create formatted string of python json object
def jprint(obj):
    text = json.dumps(obj, sort_keys = True, indent=4)
    print(text)

#display api response in json format
jprint(response.json())