from datetime import datetime
from datetime import timedelta
import nearbyPlaces
import requestForAPI
import time
import os
import responses
import json
import googlemaps
os.system("test&cls")
Hungry=float(input("How many hours ago did you eat?"))
Tired=float(input("How many hours do you drive?"))
origin=input("Where are you?")  
destination=input("Where do you want to go?")  #Üsküdar,İstanbul
while(True):
    #Gas=requestForAPI.getFuelLevel()
    Gas=5
    tirepressure=requestForAPI.getTirePressures()
    kmofcar=requestForAPI.getOdometer();
    waypoints=[]
    if(float(Gas)<10 or float(tirepressure[0])<15 or float(tirepressure[1])<15 or float(tirepressure[2])<15 or float(tirepressure[3])<15 ):
        a=nearbyPlaces.findGasStations()
        b=list(a.keys())
        location=str(a[b[0]])[1:-1]
        waypoints.append(b[0])
        Gas=100
    if(kmofcar%20000==0):
        a=nearbyPlaces.findServices()
        b=list(a.keys())
        location=str(a[b[0]])[1:-1]
        waypoints.append(b[0])
    if(Hungry>=5):
        a=nearbyPlaces.findRestaurants()
        b=list(a.keys())
        location=str(a[b[0]])[1:-1]
        waypoints.append(b[0])
        
        Hungry=0
    if(Tired>=4.30):
        a=nearbyPlaces.findSleepPlaces()
        b=list(a.keys())
        location=str(a[b[0]])[1:-1]
        waypoints.append(b[0])
        Tired=0
    
    gmaps = googlemaps.Client(key="AIzaSyDjSIZfI_fviDx3h-Wo1U9qZsK8fhHrXzA") 
    routes = gmaps.directions(origin,destination,waypoints=waypoints,optimize_waypoints=True)
    wait="BEST WAY FOR LONG WAY........\n"
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
        if(i!=len(waypoints)):
            print(waypoints[i])
        print("Estimated time: "+routes[0]["legs"][i]["duration"]["text"])
        print("-----------------------------------------------")
    Hungry+=1
    Tired+=1
    time.sleep(3600)
    
        


      
     
                  
