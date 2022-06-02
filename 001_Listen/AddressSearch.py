"""

@author: Magnus Schmid
"""

adressen = [
    "167.43.59.134",
    "164.59.134.57",
    "76.231.46.129",
    "109.65.234.65",
    "71.96.83.76"
]

gesucht = input("Gesuchte Addresse: ")

def ipvorhanden(addressen: list, gesucht: str):
    if gesucht in addressen:
        return True
    else:
        return False
    
def ipvorhanden2(addressen: list, gesucht: str):
    for item in addressen:
        if item == gesucht:
            return True  
    return False

