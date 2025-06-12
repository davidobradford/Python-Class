height1 = float(input("Enter The Height (ft) the Ball was Dropped From: "))
height2 = float(input("Enter The Height (ft) of the First Bounce: "))
bounces = int(input("Enter The Number of Bounces the Ball Took: "))

index = height2 / height1

totaldistance = 0
for count in range(bounces):
    totaldistance = totaldistance + (height1 + height2)
    height1 = height2
    height2 = height1 * index

print("The Total Distance Traveled By The Ball Is %0.2f Feet" % totaldistance) 






