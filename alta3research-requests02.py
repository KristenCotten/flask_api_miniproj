#!/usr/bin/env python3

'''
Your script alta3research-requests02.py should demonstrate proficiency with the requests HTTP library. 
This script should:
1) send a GET request to your Flask API; it should target the endpoint that returns legal JSON.
2) take the returned JSON and "normalize" it into a format that is easy for users to understand.
'''
import requests
from pprint import pprint

URL= "http://127.0.0.1:2224/dogdata"

resp= requests.get(URL).json()

pprint(resp) #display the json to see what it looks like

genus = resp[0]['genus']
species = resp[0]['species']

# display some info to the user
print(f"The scientific name for the Greyhound is {genus} {species}.")
print(f"Greyhounds are {resp[0]['characteristics'][0]}, {resp[0]['characteristics'][1]}, and from the {resp[0]['characteristics'][2]} family!")