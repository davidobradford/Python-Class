"""
File: testinputfunctions.py

Defines a function for robust input of ints.
"""

def inputInt(prompt):
    """Guarantees that the user inputs an integer,
    using the given prompt. Returns the integer."""
    while True:
        theString = input(prompt)
        if theString.isdigit():
            return int(theString)
        else:
            print("Error: the input must consist only of digits")

def inputFloat(prompt):
    """Guarantees that the user inputs either an integer or
    a floating-point number using the given prompt.
    Returns the integer."""
    while True:
        theString = input(prompt)
        if theString.isdigit():
            return int(theString)
        else:
            isFlt = True
            for ch in theString:
                if not ch.isdigit() and ch != ".":
                    isFlt = False
                    print("Error: the input must consist only of digits")
                    break
            if isFlt:
                x = theString.split(".")
                if len(x[1]) >= 2:
                    print("Error: the input must have only one decimal point")
                else:
                    return float(theString)

def main():
    n = inputFloat("Please enter a number: ")
    print(n)

if __name__ == "__main__":
    main()
