import googlemaps


def findGasStations():
    gmaps = googlemaps.Client(key='AIzaSyDjSIZfI_fviDx3h-Wo1U9qZsK8fhHrXzA')

    gmaps2 = gmaps.places_nearby(location=(41.0612191, 28.6884175), keyword="Benzin İstasyonu", language="tr",
                                 name="Benzin İstasyonu", open_now=True, rank_by="distance", type="gas_station")

    nearby_gas_stations = dict()

    for i in gmaps2['results']:
        name = i['name']
        geometry = i['geometry']
        location = geometry['location']
        lat = location['lat']
        lng = location['lng']
        nearby_gas_stations[name] = (lat, lng)

    return nearby_gas_stations


def findRestaurants():
    gmaps = googlemaps.Client(key='AIzaSyDjSIZfI_fviDx3h-Wo1U9qZsK8fhHrXzA')

    gmaps2 = gmaps.places_nearby(location=(41.0612191, 28.6884175), keyword="Yemek", language="tr",
                                 name="Yemek", open_now=True, rank_by="distance", type="restaurant")

    nearby_restaurants = dict()

    for i in gmaps2['results']:
        name = i['name']
        geometry = i['geometry']
        location = geometry['location']
        lat = location['lat']
        lng = location['lng']
        nearby_restaurants[name] = (lat, lng)

    return nearby_restaurants