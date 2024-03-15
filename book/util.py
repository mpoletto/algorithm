def swap(lyst, i, j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

def pushItem(lyst, i, j):
    """
    j is lower than i, then item in i position will be 
    pushed to j position as this will be pulled to i position
    """
    temp = lyst[j]
    lyst[j] = lyst[i]
    lyst[i] = temp