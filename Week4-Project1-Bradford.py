side1 = int(input("Enter The Length of Side One of the Triangle: "))
side2 = int(input("Enter The Length of Side Two of the Triangle: "))
side3 = int(input("Enter The Length of Side Three of the Triangle: "))

if side1 == side2 and side2 == side3:
    print("The Given Triangle IS an Equilateral Triangle.")
else:
    print("The Given Triangle IS NOT an Equilateral Triangle.")
