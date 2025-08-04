"""
Program: Week8-Project6-Bradford.py
Author: David Bradford
Deu Date: 07/13/25
Semester: Spring 2025
Instructor: Mark Pranger
Compute and print the average of numbers in a text file.
"""
def average(lyst):
    if len(lyst) == 0:
        return 0    
    avg = 0
    for y in lyst:
        avg += y
    return round(avg / len(lyst), 2) 

def main():
    fileName = input("Enter the FileName Containing the Number List: ")
    f = open(fileName, 'r')
    numberlist = []
    for line in f:
        words = line.split()
        for word in words:
            numberlist.append(int(word))
    result = average(numberlist)
    print("The average of the given number list is", result)

if __name__ == "__main__":
    main()

