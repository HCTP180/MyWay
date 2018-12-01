from datetime import datetime
from datetime import timedelta
import time

import responses
import json
import googlemaps

gmaps = googlemaps.Client(key="AIzaSyDjSIZfI_fviDx3h-Wo1U9qZsK8fhHrXzA") 
routes = gmaps.directions("Keçiören,Ankara",
                                       "Kızılay,Ankara",
                                       waypoints=["Ulus, Ankara",
                                                  "Sıhhiye, Ankara",
                                                 ],
                                       optimize_waypoints=True)
print(routes[0][][2])                   
