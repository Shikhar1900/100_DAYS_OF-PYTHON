#100 Days of Code - Project#1: Calculator Project

print ("WELCOME TO THE PYTHON CALCULATOR")

Num_1 = int(input ("Enter the First Number you want to use for the calculation: "))

Num_2 = int(input ("Enter the Second Number you want to use for the calculation: "))

SELECTION = (input ("Please select the operation: \n 1) + : Addition \n 2) - : Subtraction \n 3) * : Multiplication \n 4) / : Division \n\n SELECTION: "))

if SELECTION == "+":
    print (f"The result is: {Num_1 + Num_2}")

elif SELECTION == "-":
    print (f"The result is:  {Num_1 - Num_2}")

elif SELECTION == "*":
    Result = Num_1 * Num_2
    print (f"The result is: {Num_1 * Num_2}")

elif SELECTION == "/":
    Result = Num_1/ Num_2
    print (f"The result is: {Num_1 / Num_2}")

