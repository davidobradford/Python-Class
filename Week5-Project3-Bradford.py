import math
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
##myNumber = random.randint(smaller, larger)

myNumber = int(input("Enter the number for the computer to guess: "))
minguesses = math.log(larger, 10)
print(minguesses)

count = 0


##while True:
##    count += 1
##    userNumber = int(input("Enter your guess: "))
##    if userNumber < myNumber:
##        print("Too small!")
##    elif userNumber > myNumber:
##        print("Too large!")
##    else:
##        print("Congratulations! You've got it in", count, "tries!")
##        break
