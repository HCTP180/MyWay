import requests

token = "37bce503-105c-4e0b-8efd-17865cefc7c0"
URL = "https://api.mercedes-benz.com/experimental/connectedvehicle/v1/vehicles"
headers = {"Authorization":"Bearer " + token}
carID = requests.get(URL, headers=headers).json()[0]["id"]

def getFuelLevel():
    try:
        URL = "https://api.mercedes-benz.com/experimental/connectedvehicle/v1/vehicles"
        fuelURL = URL + "/" + str(carID) + "/" + "fuel"
        log = requests.get(fuelURL, headers=headers).json()
        return log["fuellevelpercent"]["value"]
    except Exception:
        print("Can't get fuel level!")
def getLocation():
    try:
        liste = []
        URL = "https://api.mercedes-benz.com/experimental/connectedvehicle/v1/vehicles"
        locationURL = URL + "/" + str(carID) + "/" + "location"
        log = requests.get(locationURL, headers=headers).json()
        liste.append(log["longitude"]["value"])
        liste.append(log["latitude"]["value"])
        liste.append(log["heading"]["value"])
        return liste
    except Exception:
        print("Can't get location!")
def getTirePressures():
    try:
        liste = []
        URL = "https://api.mercedes-benz.com/experimental/connectedvehicle/v1/vehicles"
        tiresURL = URL + "/" + str(carID) + "/" + "tires"
        log = requests.get(tiresURL, headers=headers).json()
        liste.append(log["tirepressurerearleft"]["value"])
        liste.append(log["tirepressurerearright"]["value"])
        liste.append(log["tirepressurefrontright"]["value"])
        liste.append(log["tirepressurefrontleft"]["value"])
        return liste
    except Exception:
        print("Can't get tire pressure!")
def getOdometer():
    try:
        URL = "https://api.mercedes-benz.com/experimental/connectedvehicle/v1/vehicles"
        odometerURL = URL + "/" + str(carID) + "/" + "odometer"
        log = requests.get(odometerURL, headers=headers).json()
        return log["odometer"]["value"]
    except Exception:
        print("Can't get odometer value!")
        
