def median(lyst):
    if len(lyst) == 0:
        return 0
    lyst.sort()
    med = len(lyst) // 2
    if len(lyst) % 2 == 1:
        return lyst[med]
    else:
        return (lyst[med] + lyst[med - 1]) / 2

def mode(lyst):
    if len(lyst) == 0:
        return 0
    numDict = {}
    for x in lyst:
        num = numDict.get(x, None)
        if num == None:
            numDict[x] = 1
        else:
            numDict[x] = num + 1
    maximum = max(numDict.values())
    mde = ""
    for x in numDict:
        if numDict[x] == maximum:
            if mde != "":
                mde = None
                break
            mde = x  
    return mde

def mean(lyst):
    if len(lyst) == 0:
        return 0    
    men = 0
    for y in lyst:
        men += y
    return round(men / len(lyst), 2) 

def main():
    fileName = input("Enter the FileName Containing the Number List: ")
    f = open(fileName, 'r')
    numberlist = []
    for line in f:
        words = line.split()
        for word in words:
            numberlist.append(int(word))
    result = median(numberlist)
    print("The median of the given number list is", result)
    result = mode(numberlist)
    print("The mode of the given number list is", result)
    result = mean(numberlist)
    print("The mean of the given number list is", result)

if __name__ == "__main__":
    main()
