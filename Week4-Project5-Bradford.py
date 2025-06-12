initpopulation = 0
growthrate = 0
hours = 0
population = 0

while initpopulation <= 0:
    initpopulation = int(input("Enter The Initial Population: "))
    if initpopulation <= 0:
        print("Initial Population Cannot Be Zero or Less, Try again...")

print(" ")
        
while growthrate <= 0:
    growthrate = float(input("Enter The Rate of Growth: "))
    if growthrate <= 0:
        print("Growth Rate Cannot Be Zero or Less, Try again...")

print(" ")

while hours <= 0:
    hours = int(input("Enter The Number of Hours The Population Grew: "))
    if hours <= 0:
        print("Hours Cannot Be Zero or Less, Try again...")
        
print(" ")

for count in range(hours + 1):
    if count == 0:
        print("Initial Population: " + str(initpopulation))
    else:
        hrs = hours * count
        population = initpopulation * growthrate * count
        print("Total Population After " + str(hrs) + " Hours " + str(population)) 






