import googlemaps

gmaps = googlemaps.Client(key='AIzaSyDjSIZfI_fviDx3h-Wo1U9qZsK8fhHrXzA')

gmaps2 = gmaps.places_nearby(location=(41.0612191,28.6884175), keyword="Benzin İstasyonu", language="tr", name="Benzin İstasyonu",open_now=True, rank_by="distance", type="gas_station")

print(gmaps2)
