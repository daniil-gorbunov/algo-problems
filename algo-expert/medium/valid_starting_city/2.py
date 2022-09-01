# medium, greedy algorithms
# time O(n) | space O(1)
def validStartingCity(distances, fuel, mpg):
    fuelLeft = 0
    minFuelLeft = 0
    startCityIdx = 0
    for cityIdx in range(1, len(fuel)):
        fuelLeft += fuel[cityIdx - 1] * mpg - distances[cityIdx - 1]
        if fuelLeft < minFuelLeft:
            minFuelLeft = fuelLeft
            startCityIdx = cityIdx
    return startCityIdx
