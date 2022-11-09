def getMinimumCost(parcels, k):
    # Write your code here
    print(parcels)
    parcels_set = set(parcels)
    minimumcost = 0
    i = 1
    remaining_parcels = k -len(parcels)
    while (remaining_parcels > 0):
        if i not in parcels_set:
            minimumcost += i
            remaining_parcels -= 1;
        i += 1
    return minimumcost    