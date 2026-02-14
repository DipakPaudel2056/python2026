# given two list of numbers one for the gas in circular form and one for the cost, you need to find the index of the gas station from where if you start the journey you can reach to the destination
def gas_station(gas,cost):
    currgas = 0
    startIndex = 0
    for i in range(len(gas)):
        currgas = currgas + gas[i] - cost[i]
        if currgas < 0:
            startIndex = i + 1
            currgas = 0
    currgas = 0
    for i in range(len(gas)):
        idx = (i + startIndex) % len(gas)
        currgas = currgas + gas[idx] - cost[idx]
        if currgas < 0:
            return -1
    
    return startIndex,gas[startIndex]

print(gas_station([4,5,7,4],[6,6,3,5]))
