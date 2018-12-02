from datetime import datetime
from datetime import timedelta
import nearbyPlaces

import time

import responses
import json
import googlemaps
Gas=8
Hungry=True
Tired=True
Service=10
waypoints=[]
if(float(Gas)<10):
    a=nearbyPlaces.findGasStations()
    b=list(a.keys())
    location=str(a[b[0]])[1:-1]
    waypoints.append(location)
if(float(Service)<15):
    a=nearbyPlaces.findServices()
    b=list(a.keys())
    location=str(a[b[0]])[1:-1]
    waypoints.append(location)
if(Hungry==True):
    a=nearbyPlaces.findRestaurants()
    b=list(a.keys())
    location=str(a[b[0]])[1:-1]
    waypoints.append(location)

if(Tired==True):
    a=nearbyPlaces.findSleepPlaces()
    b=list(a.keys())
    location=str(a[b[0]])[1:-1]
    waypoints.append(location)
    

gmaps = googlemaps.Client(key="AIzaSyDjSIZfI_fviDx3h-Wo1U9qZsK8fhHrXzA") 
routes = gmaps.directions("41.0612191, 28.6884175",
                                       "Üsküdar,İstanbul",
                                       waypoints=waypoints)
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
for i in range(len(waypoints)+1):
    print(routes[0]["legs"][i]["start_address"])
    print(routes[0]["legs"][i]["end_address"])
    print("Estimated time: "+routes[0]["legs"][i]["duration"]["text"])
    print("-----------------------------------------------")
    
        


      
     
                  
