addressen = [
    "167.43.59.134", 
    "164.59.134.57", 
    "76.231.46.129",
    "109.65.234.65", 
    "71.96.83.76"
    ]

def finder(gesucht: str, list: list):
    if gesucht in list:
        return True
    else:
        return False

gesucht = str(input("Gesuchte IP: "))
print(finder("71.96.83.76", addressen))