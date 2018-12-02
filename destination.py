from datetime import datetime
from datetime import timedelta
import nearbyPlaces

import time

import responses
import json
import googlemaps

a=nearbyPlaces.findGasStations()
Gas=False
b=list(a.keys())
location=str(a[b[0]])[1:-1]
gmaps = googlemaps.Client(key="AIzaSyDjSIZfI_fviDx3h-Wo1U9qZsK8fhHrXzA") 
routes = gmaps.directions("41.0612191, 28.6884175",
                                       "Üsküdar,İstanbul",
                                       waypoints=[location])
wait="BEST WAY FOR LONG WAY........\n"
property
process="|********************************|\n"
for l in wait:
    print(l,end="",flush=True)
    time.sleep(0.05)
print("Loading...")
for l in process:
    print(l,end="",flush=True)
    time.sleep(0.07)
for i in range(2):
    print(routes[0]["legs"][i]["start_address"])
    print(routes[0]["legs"][i]["end_address"])
    print("Estimated time: "+routes[0]["legs"][i]["duration"]["text"])
    print("-----------------------------------------------")
    
        


      
     
                  
