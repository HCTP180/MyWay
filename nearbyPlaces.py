import googlemaps


def parseJSON(JSON):
    locationDict = dict()
    try:
        for i in JSON['results']:
            name = i['name']
            geometry = i['geometry']
            location = geometry['location']
            lat = location['lat']
            lng = location['lng']
            locationDict[name] = (lat, lng)

        return locationDict
    except Exception:
        print("Can't parse JSON!")

def findGasStations():
    try:
        gmaps = googlemaps.Client(key='AIzaSyDjSIZfI_fviDx3h-Wo1U9qZsK8fhHrXzA')
        gmaps2 = gmaps.places_nearby(location=(41.0612191, 28.6884175), keyword="Benzin İstasyonu", language="tr",
                                     name="Benzin İstasyonu", open_now=True, rank_by="distance", type="gas_station")
        nearby_gas_stations = parseJSON(gmaps2)

        return nearby_gas_stations
    except Exception:
        print("Can't get gas station data from maps!")

def findRestaurants():
    try:
        gmaps = googlemaps.Client(key='AIzaSyDjSIZfI_fviDx3h-Wo1U9qZsK8fhHrXzA')
        gmaps2 = gmaps.places_nearby(location=(41.0612191, 28.6884175), keyword="Yemek", language="tr",
                                     name="Yemek", open_now=True, rank_by="distance", type="restaurant")
        nearby_restaurants = parseJSON(gmaps2)
        return nearby_restaurants
    except Exception:
        print("Can't get restaurant data from maps!")

def findServices():
    try:
        gmaps = googlemaps.Client(key='AIzaSyDjSIZfI_fviDx3h-Wo1U9qZsK8fhHrXzA')
        gmaps2 = gmaps.places_nearby(location=(41.0612191, 28.6884175), keyword="Tamir", language="tr",
                                     name="Tamir", open_now=True, rank_by="distance", type="car_repair")
        nearby_services = parseJSON(gmaps2)
        return nearby_services
    except Exception:
        print("Can't get service data from maps!")

def findSleepPlaces():
    try:
        gmaps = googlemaps.Client(key='AIzaSyDjSIZfI_fviDx3h-Wo1U9qZsK8fhHrXzA')
        gmaps2 = gmaps.places_nearby(location=(41.0612191, 28.6884175), keyword=['Hotel', 'Otel', 'Pansiyon', 'Hostel'], language="tr",
                                     name="Dinlenme", open_now=True, rank_by="distance", type="lodging")
        nearby_sleep_places = parseJSON(gmaps2)
        return nearby_sleep_places
    except Exception:
        print("Can't get place data from maps!")
