
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
    