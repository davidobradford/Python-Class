"""
Program: Week10-Project3-Bradford.py
Author: David Bradford
Due Date: 07/29/25
Semester: Spring 2025
Instructor: Mark Pranger
Convert a given temperature from Fahrenheit to Celsius OR Celsius to Fahrenheit
"""
from breezypythongui import EasyFrame

fmultiplier = 0.5556
cmultiplier = 1.8

class TempConverter(EasyFrame):
    """Computes and displays a converted tempterature, either Fahrenheit
    to Celsius OR Celsius to Fahrenheit depending on the users choice."""
    def __init__(self):
        """Set up the window and widgets."""
        EasyFrame.__init__(self, title = """Temperature Converter""")
        # Label and field for the inputs
        self.addLabel(text = "Degrees Fahrenheit",
                      row = 0, column = 0)
        self.addLabel(text = "Degrees Celsius",
                      row = 0, column = 1)
        self.inputField1 = self.addFloatField(value = 32,
                                              row = 1,
                                              column = 0,
                                              precision = 1)
        self.inputField2 = self.addFloatField(value = 0,
                                              row = 1,
                                              column = 1,
                                              precision = 1)
        # The F to C button
        self.addButton(text = ">>>>>>>", row = 2, column = 0,
                                         command = self.convertFToCTemp)
        # The C to F button
        self.addButton(text = "<<<<<<<", row = 2, column = 1,
                                         command = self.convertCToFTemp)
    # The event handling method for the first button
    def convertFToCTemp(self):
        """Inputs a Fahrenheit temp, computes
        and outputs the equivalent Celsius temp."""
        degreesF = self.inputField1.getNumber()
        degreesC = (degreesF - 32) * fmultiplier
        self.inputField2.setNumber(degreesC)
    # The event handling method for the second button
    def convertCToFTemp(self):
        """Inputs a Celsius temp, computes
        and outputs the equivalent Fahrenheit temp."""
        degreesC = self.inputField2.getNumber()
        degreesF = (degreesC * cmultiplier) + 32
        self.inputField1.setNumber(degreesF)
        
def main():
    TempConverter().mainloop()

if __name__ == "__main__":
    main()

