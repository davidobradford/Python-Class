fileName = input("Enter the Txt FileName: ")
f = open(fileName, 'r')

lines = 0
lineDict = {}
for line in f:
    lines += 1
    lineDict[lines] = line

ctr = 0
while True:
    ctr += 1
    print("The File Has", lines, "Lines")
    if lines == 0:
        break
    linenbr = int(input("Enter The Line To Display (or 0 to end): "))
    if linenbr == 0:
        break
    if linenbr > lines:
        print("There Are Not That Many Lines")
        print()
        next
    else:
        print("Line", linenbr, "Is:", lineDict[linenbr])
    



