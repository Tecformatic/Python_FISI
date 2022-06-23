from cgitb import reset
import time

temps = [
    12.5, 
    11.9, 
    11.7, 
    11.8, 
    11.6, 
    11.9, 
    12.3, 
    12.6, 
    12.9, 
    13.2,
    13.5, 
    13.8,
    13.7, 
    13.6, 
    13.7
    ]

def analyze(liste: list):
    # avg
    avg = 0
    for item in liste:
        avg = avg + item
    avg = avg / len(liste)
    
    return {
        "min": min(liste),
        "avg": avg,
        "max": max(liste)
    }


result = analyze(temps)



print(f"MIN: {result['min']:0.2f} °C\nAVG: {result['avg']:0.2f} °C\nMAX: {result['max']:0.2f} °C")
print(result)