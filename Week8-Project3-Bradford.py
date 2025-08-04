"""
Program: Week8-Project3-Bradford.py
Author: David Bradford
Deu Date: 07/13/25
Semester: Spring 2025
Instructor: Mark Pranger
Return Tue or false if a Given List is Sorted or Not.
"""
def isSorted(lyst):
    
    numitems = len(lyst)
    isSrtd = True
    
    if numitems == 0 or numitems == 1:
        return True
    
    ctr = 0
    while (ctr != numitems - 1):
        if lyst[ctr] > lyst[ctr + 1]:
            return False
        ctr += 1
    return True
            
        
