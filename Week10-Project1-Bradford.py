"""
Program: Week10-Project1-Bradford.py
Author: David Bradford
Due Date: 07/29/25
Semester: Spring 2025
Instructor: Mark Pranger
Tax calculator Program - GUI based
"""
from breezypythongui import EasyFrame
import math

taxrate = 0.20
std_deduction = 10000.0
dep_deduction = 3000.0

class TaxCalculator(EasyFrame):
    """Computes and displays the Tax based On A Given Gross Income and
    Number of Dependants."""
    
    def __init__(self):
        """Set up the window and widgets."""
        EasyFrame.__init__(self, title = """Tax Calculator""")
        # Label and field for the inputs
        self.addLabel(text = "Gross Income",
                      row = 0, column = 0)
        self.inputField1 = self.addFloatField(value = 0,
                                             row = 0,
                                             column = 1,
                                             width = 20)
        self.addLabel(text = "Dependents",
                      row = 1, column = 0)
        self.inputField2 = self.addIntegerField(value = 0,
                                               row = 1,
                                               column = 1,
                                               width = 10)
        # The command button
        self.addButton(text = "Compute", row = 3, column = 0,
                       columnspan = 2,
                       command = self.computeTax)
        # Label and field for the output
        self.addLabel(text = "Total Tax",
                      row = 4, column = 0)
        self.outputField = self.addFloatField(value = 0.0,
                                              row = 4,
                                              column = 1,
                                              width = 20,
                                              precision = 2,
                                              state = "readonly")
    
    # The event handling method for the button
    def computeTax(self):
        """Inputs the Gross Income and Number of Dependents, computes
        and outputs the Income Tax."""
        grossamt = self.inputField1.getNumber()
        dependents = self.inputField2.getNumber()
        taxableIncome = grossamt - std_deduction - \
                                dep_deduction * dependents
        incomeTax = taxableIncome * taxrate
        self.outputField.setNumber(incomeTax)
            
def main():
    TaxCalculator().mainloop()

if __name__ == "__main__":
    main()

