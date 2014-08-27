import math

def detour(pointA, pointB, pointC, pointD):
    driver1dist = getDistance(pointA, pointB)    
    driver1detour = getDistance(pointA, pointC) + getDistance(pointC, pointD)
    
    driver2dist = getDistance(pointC, pointD)
    driver2detour = getDistance(pointB, pointA) + getDistance(pointA, pointD)

    driver1diff = max(0, driver1detour - driver1dist)
    driver2diff = max(0, driver2detour - driver2dist)

    if driver1diff < driver2diff:
        print "Driver 1 should take the detour, distance = {}".format(driver1diff)
    elif driver1diff > driver2diff:
        print "Driver 2 should take the detour, distance = {}".format(driver2diff)
    else:
        print "The detour distances are equal, distance = {}".format(driver1diff)


def getDistance(pointA, pointB):
    xdif = pointA.lat - pointB.lat
    ydif = pointA.lon - pointB.lon
    distance = pythagorean(xdif, ydif)
    print(distance)
    return distance

def pythagorean(x, y):
    zsqr= x*x + y*y
    return math.sqrt(zsqr)

class Point:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

pointA = Point(3, 6)
pointB = Point(6, 10)
pointC = Point(12, 18)
pointD = Point(9, 14)

detour(pointA, pointB, pointC, pointD)
