# medium, greedy algorithms
# time O(n^2) | space O(1)
def validStartingCity(distances, fuel, mpg):
    numCities = len(distances)
    for startCityIdx in range(numCities):
        endCityIdx = (startCityIdx + numCities - 1) % numCities
        currentCityIdx = startCityIdx
        fuelLeft = 0
        while currentCityIdx != endCityIdx:
            fuelLeft += fuel[currentCityIdx] * mpg - distances[currentCityIdx]
            if fuelLeft < 0:
                break
            currentCityIdx = (currentCityIdx + 1) % numCities
        if currentCityIdx == endCityIdx:
            return startCityIdx
