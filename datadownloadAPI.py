# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 11:27:07 2019

@author: saksh
"""

import requests

url = "https://api.crunchbase.com/v3.1/organizations?user_key=49582f4b8512004b9965458f747b27f6"

response = requests.request("GET", url)

print(response.text)

print(response.status_code)
output=response.json()

data=json.loads(output.text)
#python date time module
#pandas to json


import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


text=jprint(response.json())


input_dict = json.loads(response.text)
print(json.dumps(input_dict))

print(input_dict)
output_dict = [x for x in input_dict if x['updated_at']=1575036875]
