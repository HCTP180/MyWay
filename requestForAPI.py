import requests

def getFuelLevel(json):
    return json["fuellevelpercent"]["value"]

def getLocation(json):
    liste = []
    liste.append(json["longitude"]["value"])
    liste.append(json["latitude"]["value"])
    liste.append(json["heading"]["value"])
    return liste
    
def getTirePressures(json):
    liste = []
    liste.append(json["tirepressurerearleft"]["value"])
    liste.append(json["tirepressurerearright"]["value"])
    liste.append(json["tirepressurefrontright"]["value"])
    liste.append(json["tirepressurefrontleft"]["value"])
    return liste

def getOdometer(json):
    return json["odometer"]["value"]
    
token = "8c92ef33-65bc-48d9-953e-662dc55495d2"
URL = "https://api.mercedes-benz.com/experimental/connectedvehicle/v1/vehicles"


headers = {"Authorization":"Bearer " + token}
carID = requests.get(URL, headers=headers).json()[0]["id"]

tiresURL = URL + "/" + str(carID) + "/" + "tires"
locationURL = URL + "/" + str(carID) + "/" + "location"
fuelURL = URL + "/" + str(carID) + "/" + "fuel"
stateofchargeURL = URL + "/" + str(carID) + "/" + "stateofcharge"
doorsURL = URL + "/" + str(carID) + "/" + "doors"
odometerURL = URL + "/" + str(carID) + "/" + "odometer"

# print(tiresURL)
# print(locationURL)
# print(fuelURL)
# print(stateofchargeURL)
# print(doorsURL)
# print(odometerURL)

log = requests.get(tiresURL, headers=headers).json()
print(getTirePressures(log))

log = requests.get(locationURL, headers=headers).json()
print(getLocation(log))

log = requests.get(fuelURL, headers=headers).json()
print(getFuelLevel(log))

log = requests.get(stateofchargeURL, headers=headers).json()
print(log)

log = requests.get(doorsURL, headers=headers).json()
print(log)

log = requests.get(odometerURL, headers=headers).json()
print(getOdometer(log))
