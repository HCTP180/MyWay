import requests

def getFuelLevel():
    URL = "https://api.mercedes-benz.com/experimental/connectedvehicle/v1/vehicles"
    fuelURL = URL + "/" + str(carID) + "/" + "fuel"
    log = requests.get(fuelURL, headers=headers).json()
    #print(log)
    return log["fuellevelpercent"]["value"]

def getLocation():
    liste = []
    URL = "https://api.mercedes-benz.com/experimental/connectedvehicle/v1/vehicles"    
    locationURL = URL + "/" + str(carID) + "/" + "location"
    log = requests.get(locationURL, headers=headers).json()
    #print(log)
    liste.append(log["longitude"]["value"])
    liste.append(log["latitude"]["value"])
    liste.append(log["heading"]["value"])
    return liste
    
def getTirePressures():
    liste = []
    URL = "https://api.mercedes-benz.com/experimental/connectedvehicle/v1/vehicles"
    tiresURL = URL + "/" + str(carID) + "/" + "tires"
    log = requests.get(tiresURL, headers=headers).json()
    #print(log)
    liste.append(log["tirepressurerearleft"]["value"])
    liste.append(log["tirepressurerearright"]["value"])
    liste.append(log["tirepressurefrontright"]["value"])
    liste.append(log["tirepressurefrontleft"]["value"])
    return liste

def getOdometer():
    URL = "https://api.mercedes-benz.com/experimental/connectedvehicle/v1/vehicles"
    odometerURL = URL + "/" + str(carID) + "/" + "odometer"
    log = requests.get(odometerURL, headers=headers).json()
    #print(log)
    return log["odometer"]["value"]
        
token = "37bce503-105c-4e0b-8efd-17865cefc7c0"
URL = "https://api.mercedes-benz.com/experimental/connectedvehicle/v1/vehicles"
headers = {"Authorization":"Bearer " + token}
carID = requests.get(URL, headers=headers).json()[0]["id"]
