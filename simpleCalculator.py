"""----------------------------------------------------------------------
Name: Sean Casaus
File Name: simpleCalculator.py
Specifications: A simple Calculator where the user enters two operands and
    chooses from a menu to add, subtract, multiply, or divide the inputs.
Time Spent: 1 hour
----------------------------------------------------------------------"""
import math
import decimal

#Takes in user input for two operands
print "Welcome to the Calculator"
firstOperand = input("Enter the first operand: ")
secondOperand = input("Enter the second operand: ")
print " "

#Prints the operations menu
print "Operations are: "
print "ADD or + for addition"
print "SUBTRACT or - for subtraction"
print "MULTIPLY or * for multiplication"
print "DIVIDE or / for division"

#User input for operation
selection = raw_input("Enter your selection: ")
selection

#If addition is chosen program prints sum
if selection == "add" or selection == "+":
    result = float(firstOperand) + secondOperand
    result = str('%.3g'%(result))
    print "The sum is " + result

#If subtraction is chosen program prints difference
elif selection == "subtract" or selection == "-":
    result = float(firstOperand) - secondOperand
    result = str('%.3g'%(result))
    print "The difference is " + result

#If multiplication is chosen program prints product
elif selection == "multiply" or selection == "*":
    result = float(firstOperand) * secondOperand
    result = str('%.3g'%(result))
    print "The product is " + result

#If division is chosen program prints quotient
elif selection == "divide" or selection == "/":
    result = float(firstOperand) / secondOperand
    result = str('%.3g'%(result))
    print "The quotient is " + result

#if user inputs invalid option, program prints statement
else:
    print "Invalid Entry!"

raw_input("Press<enter>")
