from math import sqrt


def calcHypotenuse(a: float, b: float) -> float:
    """
    Berechnet die Grundseite eines rechtwinkligen Dreiecks
    """
    asqr = a**2
    bsqr = b**2
    csqr = asqr + bsqr
    return sqrt(csqr)

def calcCuboidVolume(a: float, b: float, c: float) -> float:
    """
    Calculates the Volume of a Cuboid
    """
    return a*b*c

def calcFrameVolume(height: float, width: float, depth: float, thickness: float) -> float:
    Vges = height * width * depth
    Vin = (height - 2 * thickness) * (width - 2 * thickness) * depth
    return Vges - Vin
